# Shopping

Predicts whether an online shopping session will end in a purchase, using a k-nearest-neighbour classifier (k = 1) trained on user browsing data.

## Usage

```bash
pip install scikit-learn
python shopping.py shopping.csv
```

Example output:

```
Correct: 4088
Incorrect: 844
True Positive Rate: 41.02%
True Negative Rate: 90.55%
```

Results vary slightly between runs because the train/test split is random.

## How it works

- **`load_data(filename)`** reads the CSV with `csv.DictReader` and turns each row into 17 numeric features plus a label:
  - Page counts and durations are converted to `int` / `float`
  - `Month` becomes an index from 0 (Jan) to 11 (Dec); the first three letters are used because the data spells June as `June`
  - `VisitorType` becomes 1 for `Returning_Visitor`, otherwise 0
  - `Weekend` and `Revenue` become 1 for `TRUE`, otherwise 0
- **`train_model(evidence, labels)`** fits a `KNeighborsClassifier(n_neighbors=1)`.
- **`evaluate(labels, predictions)`** returns:
  - **Sensitivity** (true positive rate): correctly predicted purchases ÷ actual purchases
  - **Specificity** (true negative rate): correctly predicted non-purchases ÷ actual non-purchases
- **`main()`** holds back 40% of the data for testing (`TEST_SIZE = 0.4`), trains on the rest and prints the results.

## Notes

- Specificity is much higher than sensitivity because most sessions don't end in a purchase, so the model sees far more negative examples.
- Features aren't scaled, so columns with large values (such as durations) dominate the distance calculation; scaling them is an easy possible improvement.