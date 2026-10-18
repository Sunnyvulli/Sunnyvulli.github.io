import csv, json, sqlite3, tempfile, unittest, threading, urllib.request, urllib.error
from pathlib import Path
from http.server import HTTPServer
from pipeline import run, validate, FIELDS
from api import Handler


class SystemTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.db = Path(self.tmp.name) / "m.sqlite"
        self.source = Path(__file__).parent / "data/hour.csv"
        with self.source.open() as f:
            self.raw = list(csv.DictReader(f))

    def test_real_data_reconciles(self):
        r, s = run(self.source, self.db)
        self.assertFalse(s)
        self.assertEqual(r["input_rows"], 17379)
        self.assertEqual(r["accepted_rows"] + r["rejected_rows"], 17379)
        self.assertEqual(r["rejected_rows"], 0)
        self.assertEqual(r["rentals"], sum(int(x["cnt"]) for x in self.raw))

    def test_cache_is_idempotent(self):
        a, _ = run(self.source, self.db)
        b, s = run(self.source, self.db)
        self.assertTrue(s)
        self.assertEqual(a, b)

    def test_fault_types(self):
        rows = [r.copy() for r in self.raw[:4]]
        rows[0]["hr"] = "25"
        rows[1]["cnt"] = "999999"
        rows[2]["hum"] = "NaN"
        rows.append(rows[3].copy())
        good, bad = validate(rows)
        self.assertEqual(len(good), 1)
        self.assertEqual(len(bad), 4)

    def test_bad_schema_preserves_snapshot(self):
        run(self.source, self.db)
        p = Path(self.tmp.name) / "bad.csv"
        p.write_text("x\n1\n")
        with self.assertRaises(ValueError):
            run(p, self.db)
        with sqlite3.connect(self.db) as d:
            self.assertEqual(
                d.execute("select count(*) from observations").fetchone()[0], 17379
            )

    def test_empty_batch_preserves_snapshot(self):
        run(self.source, self.db)
        p = Path(self.tmp.name) / "empty.csv"
        p.write_text(",".join(FIELDS) + "\n")
        with self.assertRaises(ValueError):
            run(p, self.db)

    def test_actual_http(self):
        run(self.source, self.db)
        s = HTTPServer(("127.0.0.1", 0), Handler)
        s.database = self.db
        t = threading.Thread(target=s.serve_forever, daemon=True)
        t.start()
        try:
            u = "http://127.0.0.1:" + str(s.server_port)
            with urllib.request.urlopen(u + "/health") as r:
                self.assertEqual(json.load(r)["rows"], 17379)
            with urllib.request.urlopen(
                u + "/daily?start=2011-01-01&end=2011-01-01"
            ) as r:
                self.assertEqual(len(json.load(r)["data"]), 1)
            with self.assertRaises(urllib.error.HTTPError) as c:
                urllib.request.urlopen(u + "/daily?start=invalid")
            self.assertEqual(c.exception.code, 400)
            with self.assertRaises(urllib.error.HTTPError) as c:
                urllib.request.urlopen(u + "/missing")
            self.assertEqual(c.exception.code, 404)
        finally:
            s.shutdown()
            s.server_close()
            t.join()


if __name__ == "__main__":
    unittest.main()
