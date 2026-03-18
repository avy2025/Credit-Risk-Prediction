import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib
import json
import os

def train():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data"
    columns = [
        'Status', 'Duration', 'CreditHistory', 'Purpose', 'CreditAmount',
        'Savings', 'Employment', 'InstallmentRate', 'PersonalStatus',
        'OtherDebtors', 'ResidenceSince', 'Property', 'Age',
        'OtherInstallmentPlans', 'Housing', 'ExistingCredits',
        'Job', 'Dependents', 'Telephone', 'ForeignWorker', 'Target'
    ]
    df = pd.read_csv(url, sep=' ', names=columns)
    df['Target'] = df['Target'].map({1: 0, 2: 1})

    X = df.drop('Target', axis=1)
    y = df['Target']

    categorical_cols = X.select_dtypes(include='object').columns
    numerical_cols = X.select_dtypes(exclude='object').columns

    # Capture original feature metadata for UI
    feature_metadata = {}
    for col in columns[:-1]:
        if col in categorical_cols:
            feature_metadata[col] = {
                "type": "categorical",
                "options": sorted(df[col].unique().tolist())
            }
        else:
            feature_metadata[col] = {
                "type": "numerical",
                "min": int(df[col].min()),
                "max": int(df[col].max())
            }

    # One-hot encoding
    X_encoded = pd.get_dummies(X, columns=categorical_cols, drop_first=True)
    trained_columns = X_encoded.columns.tolist()

    # Train Random Forest
    rf_model = RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        random_state=42,
        class_weight='balanced'
    )
    rf_model.fit(X_encoded, y)

    # Save artifacts
    os.makedirs('models', exist_ok=True)
    joblib.dump(rf_model, 'models/model.joblib')
    joblib.dump(trained_columns, 'models/columns.joblib')
    
    with open('models/metadata.json', 'w') as f:
        json.dump(feature_metadata, f, indent=4)

    print("Model training complete. Artifacts saved in 'models/' directory.")

if __name__ == "__main__":
    train()
