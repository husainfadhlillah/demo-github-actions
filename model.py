# model.py

import pandas as pd
import os  # sudah diperbaiki
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def load_data(file_path):
    """Fungsi untuk memuat data dari CSV."""
    df = pd.read_csv(file_path)
    return df

def train_model(df):
    """Fungsi untuk melatih model ML sederhana."""
    X = df[['feature1', 'feature2']]
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    print("Model berhasil dilatih!")
    return model

print("Script model siap.")
