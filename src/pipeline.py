import argparse
from pathlib import Path
import joblib
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.model_selection import train_test_split

FEATURES = ["Store", "Dept", "IsHoliday", "Size", "Temperature", "Fuel_Price", "CPI", "Unemployment"]

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["Date"] = pd.to_datetime(df["Date"])
    df["IsHoliday"] = df["IsHoliday"].astype(int)
    return df

def prepare(df: pd.DataFrame):
    clean = df[FEATURES + ["Weekly_Sales"]].copy()
    clean = clean.dropna()
    X = clean[FEATURES]
    y = clean["Weekly_Sales"]
    return X, y

def train(path: str, output: str):
    df = load_data(path)
    X, y = prepare(df)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = GradientBoostingRegressor(random_state=42, n_estimators=180, max_depth=3)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    metrics = {"r2": r2_score(y_test, pred), "mae": mean_absolute_error(y_test, pred)}
    Path(output).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump({"model": model, "features": FEATURES, "metrics": metrics}, output)
    print(metrics)
    return metrics

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/train.csv")
    parser.add_argument("--output", default="artifacts/model.joblib")
    args = parser.parse_args()
    train(args.input, args.output)
