# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wa4bJ48Fcf_JJF37h99kTPKH8F4h-fbP

Supervised Pipeline
"""

#Import the necessary Libraries

import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

#Load the data

data = pd.read_csv('/content/creditcard.csv')  # Add error handling

# Select only the 'Time', 'Amount', and 'Class' columns
data = data[['Time', 'Amount', 'Class']]

# Drop rows where the target variable 'Class' is NaN
data = data.dropna(subset=['Class'])

# Separate features and target
x = data[['Time', 'Amount']]
y = data['Class']

# Verify that there are no NaN values in the target variable
print(y.isna().sum())

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Create a pipeline with SMOTE and RandomForestClassifier
pipeline_rf = Pipeline([
    ('sm', SMOTE(random_state=42)),
    ('rf', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Create a pipeline with SMOTE and XGBoostClassifier
pipeline_xgb = Pipeline([
    ('sm', SMOTE(random_state=42)),
    ('xgb', XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42))
])

# Fit the pipelines to the training data
pipeline_rf.fit(x_train, y_train)
pipeline_xgb.fit(x_train, y_train)

# Predict the testing data
y_pred_rf = pipeline_rf.predict(x_test)
y_pred_xgb = pipeline_xgb.predict(x_test)

# Evaluate the models
print("Random Forest Classification Report: \n", classification_report(y_test, y_pred_rf))

# Plot confusion matrices
def plot_confusion_matrix(y_true, y_pred, title):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title(title)
    plt.show()

# Plot confusion matrices for Random Forest and XGBoost
plot_confusion_matrix(y_test, y_pred_rf, "Random Forest Confusion Matrix")

accuracy_rf = accuracy_score(y_test, y_pred_rf)
print(f"Random Forest Accuracy: {accuracy_rf}")

print("XGBoost Classification Report: \n", classification_report(y_test, y_pred_xgb))

plot_confusion_matrix(y_test, y_pred_xgb, "XGBoost Confusion Matrix")

accuracy_xgb = accuracy_score(y_test, y_pred_xgb)

print(f"XGBoost Accuracy: {accuracy_xgb}")

# Save the models
joblib.dump(pipeline_rf, 'rf_pipeline.pkl')
print("Random Forest pipeline has been saved as rf_pipeline.pkl")
joblib.dump(pipeline_xgb, 'xgb_pipeline.pkl')
print("XGBoost pipeline has been saved as xgb_pipeline.pkl")

"""Unsupervised Pipeline"""

#import the necessary libraries

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

#load the data
data = pd.read_csv('/content/creditcard.csv', on_bad_lines='warn')

# Select only the 'Time', 'Amount', and 'Class' columns
data = data[['Time', 'Amount', 'Class']]

# Drop rows where the target variable is NaN
data = data.dropna(subset=['Class'])

# Separate features and target
x = data[['Time', 'Amount']]
y = data['Class']

# Verify that there are no NaN values in the target variable
print(y.isna().sum())

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42, stratify=y)

# Create a pipeline with StandardScaler and IsolationForest
pipeline_if = Pipeline([
    ('sc', StandardScaler()),
    ('if', IsolationForest(contamination=0.1, random_state=42))
])

# Create a pipeline with StandardScaler and LocalOutlierFactor
pipeline_lof = Pipeline([
    ('sc', StandardScaler()),
    ('lof', LocalOutlierFactor(n_neighbors=20, contamination=0.1, novelty=True))
])

# Fit the pipelines to the training data
pipeline_if.fit(x_train)
pipeline_lof.fit(x_train)

# Predict the testing data
y_pred_if = pipeline_if.named_steps['if'].predict(x_test)
y_pred_lof = pipeline_lof.named_steps['lof'].predict(x_test)

# Transform predictions to match expected format (1 for inliers, -1 for outliers)
y_pred_if = (y_pred_if == 1).astype(int)
y_pred_if = (y_pred_if - 0.5) * 2
y_pred_lof = (y_pred_lof == 1).astype(int)
y_pred_lof = (y_pred_lof - 0.5) * 2

# Evaluate the models
print("Isolation Forest Classification Report: \n", classification_report(y_test, y_pred_if))

# Plot confusion matrices
def plot_confusion_matrix(y_true, y_pred, title):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title(title)
    plt.show()

# Plot confusion matrices for Random Forest and XGBoost
plot_confusion_matrix(y_test, y_pred_if, "Isolation Forest Confusion Matrix")

print("Local Outlier Factor Classification Report: \n", classification_report(y_test, y_pred_lof))

plot_confusion_matrix(y_test, y_pred_lof, "Local Outlier Factor Confusion Matrix")

# Save the models
joblib.dump(pipeline_if, 'if_pipeline.pkl')
print("Isolation Forest pipeline has been saved as if_pipeline.pkl")
joblib.dump(pipeline_lof, 'lof_pipeline.pkl')
print("Local Outlier Factor pipeline has been saved as lof_pipeline.pkl")