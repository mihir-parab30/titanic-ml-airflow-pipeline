import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

DATA_DIR = "/opt/airflow/data"
os.makedirs(DATA_DIR, exist_ok=True)

def download_data():
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    df = pd.read_csv(url)
    df.to_csv(f"{DATA_DIR}/titanic.csv", index=False)
    print("✅ Titanic dataset downloaded.")

def preprocess_data():
    df = pd.read_csv(f"{DATA_DIR}/titanic.csv")
    df = df.dropna(subset=["Age", "Embarked"])
    le_sex = LabelEncoder()
    df["Sex"] = le_sex.fit_transform(df["Sex"])
    le_embarked = LabelEncoder()
    df["Embarked"] = le_embarked.fit_transform(df["Embarked"])
    df.to_csv(f"{DATA_DIR}/titanic_clean.csv", index=False)
    print("✅ Data preprocessed and saved.")

def train_model():
    df = pd.read_csv(f"{DATA_DIR}/titanic_clean.csv")
    X = df[["Pclass", "Sex", "Age", "Fare", "Embarked"]]
    y = df["Survived"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    joblib.dump(model, f"{DATA_DIR}/titanic_model.pkl")
    print("✅ Model trained and saved.")

def evaluate_model():
    df = pd.read_csv(f"{DATA_DIR}/titanic_clean.csv")
    X = df[["Pclass", "Sex", "Age", "Fare", "Embarked"]]
    y = df["Survived"]
    model = joblib.load(f"{DATA_DIR}/titanic_model.pkl")
    preds = model.predict(X)
    acc = accuracy_score(y, preds)
    print(f"✅ Model accuracy on full data: {acc:.2f}")