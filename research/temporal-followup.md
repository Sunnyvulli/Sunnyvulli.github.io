# Whole-day temporal validation: Mobility Quality Lab follow-up

**Status:** executed portfolio experiment; unpublished technical note. 18 October 2026.

## Why this iteration exists
The initial study used one chronological holdout that could split a day and included observed same-hour weather. That supports retrospective estimation, not an operational forecasting claim. This follow-up adds whole-day windows, a seasonal baseline, and a calendar-only model. It is a separate experiment; its errors must not be compared directly with the original weather-based model as though the evaluation sets/features were identical.

## Question
In three defined historical 28-day windows, how does a calendar-only forest compare with a training-mean baseline and a same-hour, previous-week count?

## Protocol
- Starts: April 1, July 1, and October 1, 2012. Each test window is [start, start + 28 days); no test days overlap.
- Expanding training history includes only timestamps strictly before each test-window boundary.
- Test observations: 670, 672, and 672 hourly records, covering 84 days in total. The first window lacks two hourly records; missing outcomes are not imputed.
- Calendar features: season, year indicator, month, hour, holiday, weekday, working-day indicator. Weather, record ID, casual counts, registered counts, and current target are excluded.
- Forest: 60 trees, max depth 16, minimum leaf size 2, one worker, seeds 11/23/37. Models are trained once at each window boundary. No hyperparameter search is claimed.
- Mean baseline: training-set mean for that fold.
- Weekly baseline: observed count at the same local clock hour seven calendar days earlier. If absent, use the training-only weekday/hour mean, then the training-only overall mean. Two fallbacks occur in April; none in the other folds.

**Information availability matters:** this is an online one-hour-ahead evaluation protocol with seven-day-old counts available as each prediction is made. For test days after the first week, the weekly baseline can use earlier observed outcomes inside that same test window. It is not a fixed 28-day-ahead forecast. The forest remains fixed within a window and does not consume those outcome updates. Timestamps follow the source's naive clock convention; no timezone/DST reconstruction is attempted.

## Executed results
Metrics are weighted by observed test-row counts. Forest metrics additionally average the three seeded runs. RMSE is obtained from the pooled weighted squared error, not the mean of fold RMSE values.

| Model | Weighted MAE, rentals/hour | Weighted RMSE, rentals/hour | Evaluations |
|---|---:|---:|---:|
| Training mean | 184.222 | 242.062 | 3 |
| Weekly lag, online | 64.031 | 105.433 | 3 |
| Calendar-only forest | 49.766 | 84.301 | 9 |

The observed MAE reduction from weekly baseline to forest is approximately 22.3% on these windows. This is a historical comparison, not a promise of future accuracy, financial savings, or real-world adoption.

## Uncertainty analysis
Compute each day's average absolute error; forest daily errors are averaged over seeds. There are 84 paired daily differences (forest minus weekly). Their equally weighted mean is -14.269 rentals/hour. A 2,000-replicate percentile bootstrap, seed 101, gives [-22.513, -6.596]. This daily-weighted quantity differs slightly from the row-weighted MAE difference.

The bootstrap assumes exchangeable days and does not model serial dependence, overlapping training windows, or source representativeness. The interval is exploratory, not a validated population confidence guarantee or a significance claim. A time-block bootstrap and more origins are needed for stronger inference.

## Reproduction and checks
After installing projects/mobility-quality/requirements.txt, run `make backtest` from the repository root. Results are committed as temporal-evaluation.json and temporal-daily-errors.csv in that project's results directory. They record file hash, package versions, seeds, fold boundaries, fallback counts, individual runs, and bootstrap settings. CI executes this study after the original evaluation.

Three new protocol tests check whole-day windows with strictly past training, lag usage independent of the current target, and training-only fallback. Together with the seven pipeline/API tests, ten tests run in the smoke path and container.

## Interpretation and next work
Calendar structure can be a strong baseline signal in this historical system-wide series. The experiment does not establish a deployable demand predictor: it excludes capacity constraints, station-level movements, current ridership, covariate drift, delayed labels, weather forecasts, and a service-cost objective. The three starts are specified study windows, not a representative random sample of seasons/years. Do not turn the favorable aggregate into a general claim.

Next work: more rolling origins, time-block uncertainty, explicit label-delay sensitivity, a matched lag-feature model, and a second licensed dataset. Those experiments have not been run here.

## Attribution
Dataset: Fanaee-T, H. (2013). Bike Sharing [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5W894 . CC BY 4.0; hashes and source details in projects/mobility-quality/data/SOURCE.md. Algorithms use scikit-learn, not a claimed new forecasting method. Evaluation context and prior work are cited in the initial manuscript research/mobility-study.md.
