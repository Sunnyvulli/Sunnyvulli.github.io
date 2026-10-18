# Build note: improve the evaluation before improving the model

The first Mobility Quality Lab release made data contracts and target leakage inspectable. Its next weakness was evaluation: one chronological split could divide a day, while contemporaneous weather made the model a retrospective estimator.

This iteration changes the question. Three 28-day windows start at midnight; training uses only earlier observations. A mean predictor and an online weekly-lag predictor establish meaningful baselines. The new forest uses only calendar variables, keeping current weather and target components out of the feature set.

Across 84 historical test days, the forest achieved a row-weighted MAE of 49.766 rentals/hour, versus 64.031 for the weekly baseline. The useful result is not just the lower number: source hashes, boundaries, per-run measurements, fallback behavior, tests, and limitations are available for inspection.

The weekly baseline uses outcomes from seven days earlier as time advances. That makes it valid for the stated online protocol, not for a 28-day-ahead forecast. Two missing lag observations require a fallback learned only from the training data. A paired daily bootstrap is included, but it does not account for temporal dependence; it should not be used to claim statistical certainty.

Three protocol tests now protect against crossing training boundaries, accidentally reading the current target, and using holdout outcomes for fallback averages. The same tests run in CI and in the container. The project remains a historical local reference implementation.

- [Complete protocol and limitations](../research/temporal-followup.md)
- [Implementation](../projects/mobility-quality/temporal.py)
- [Raw results](../projects/mobility-quality/results/temporal-evaluation.json)

The next step is broader origins and time-block uncertainty, not a claim that one favorable backtest is production proof.
