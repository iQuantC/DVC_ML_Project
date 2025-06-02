import pandas as pd
from joblib import load
from sklearn.metrics import accuracy_score
import json

X_test = pd.read_csv("data/X_test.csv")
y_test = pd.read_csv("data/y_test.csv")

model = load("model/model.joblib")
predictions = model.predict(X_test)

acc = accuracy_score(y_test, predictions)

with open("metrics.json", "w") as f:
    json.dump({"accuracy": acc}, f)
