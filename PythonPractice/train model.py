import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Load the dataset
df = pd.read_csv("admissions.csv")

# 2. Separate input features and target
X = df[
    [
        "cgpa",
        "ielts_overall",
        "projects",
        "internship",
        "research"
    ]
]

y = df["admission_outcome"]

# 3. Identify feature types
numeric_features = [
    "cgpa",
    "ielts_overall",
    "projects"
]

categorical_features = [
    "internship",
    "research"
]

# 4. Convert categorical values into numerical features
preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)

# 5. Create the Random Forest model
random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    max_depth=5
)

# 6. Combine preprocessing and model
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", random_forest)
    ]
)

# 7. Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 8. Train the model
model.fit(X_train, y_train)

# 9. Predict outcomes for test records
y_pred = model.predict(X_test)

# 10. Evaluate the model
accuracy = accuracy_score(y_test, y_pred)

print("Random Forest Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# 11. Save the trained pipeline
joblib.dump(model, "admission_model.pkl")

print("\nModel saved successfully!")