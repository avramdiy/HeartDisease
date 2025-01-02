# model.py

import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load data
file_path = r"C:\\Users\\Ev\\Desktop\\HeartDisease\\heart_disease.csv"
df = pd.read_csv(file_path)

# Preprocessing
df.dropna(subset=['Blood Pressure', 'Age', 'BMI', 'Gender'], inplace=True)

# Encoding categorical data (Gender)
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})

# Features and target
X = df[['Age', 'BMI', 'Gender']]  # Predictors
y = df['Blood Pressure']  # Target variable

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Save the model
with open("blood_pressure_model.pkl", "wb") as f:
    pickle.dump(model, f)
