import pandas as pd
from sklearn.linear_model import LogisticRegression
from joblib import dump

X_train = pd.read_csv("data/X_train.csv")
y_train = pd.read_csv("data/y_train.csv").values.ravel()

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

dump(model, "model/model.joblib")
