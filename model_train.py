import pandas as pd
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
import pickle

# Load dataset
df = pd.read_csv("housing.csv")

# Separate features and target
X = df.drop("MEDV", axis=1)
y = df["MEDV"]

# Create pipeline with imputer, scaler, and Lasso
model = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),    # Handle NaNs
    ("scaler", StandardScaler()),
    ("lasso", Lasso(alpha=0.1))
])

# Train the model
model.fit(X, y)

# Save the model to a file
pickle.dump(model, open("model.pkl", "wb"))

