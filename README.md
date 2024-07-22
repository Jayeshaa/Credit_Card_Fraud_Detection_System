# Credit_Card_Fraud_Detection_System

The Credit Card Fraud Detection System is designed to identify fraudulent credit card transactions using machine learning techniques. This system utilizes both supervised and unsupervised learning methods to detect anomalies and potential frauds in transaction data. The entire system is built using Python and is deployed as an interactive web application using Streamlit.

# Key Features

Data Preprocessing

NumPy and Pandas: Used for efficient data manipulation, cleaning, and preprocessing. This includes handling missing values, normalizing features, and splitting the data into training and testing sets.

Supervised Learning

Random Forest: An ensemble learning method that builds multiple decision trees and merges them to get a more accurate and stable prediction.

XGBoost: A gradient boosting framework that is highly efficient and effective for classification tasks.

Unsupervised Learning

Isolation Forest: Detects anomalies by isolating observations in the data. Anomalies are isolated more quickly than normal points.

Local Outlier Factor (LOF): Identifies anomalies by measuring the local density deviation of a given data point with respect to its neighbors.

Deployment

Streamlit: Provides an interactive web interface where users can input transaction details and receive immediate fraud detection results.

Set up Twilio:

Create a Twilio account and obtain your Account SID, Auth Token, and phone number.
Set the environment variables TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, and TWILIO_PHONE_NUMBER in your .env file.

Functionality

Data Preprocessing:

Load and clean the credit card transaction data using NumPy and Pandas.
Prepare the data for modeling, including feature scaling and encoding.
Model Pipelines:

Supervised Pipeline: Trains Random Forest and XGBoost models on labeled data to predict fraudulent transactions.
Unsupervised Pipeline: Uses Isolation Forest and LOF to detect anomalies in unlabeled data.
Fraud Detection:

Analyze transactions using both supervised and unsupervised models.
Determine if a transaction is fraudulent based on the model predictions.
SMS Alerts:

Integrates with Twilio to send SMS alerts to users if a transaction is detected as fraudulent.
Notifications include details about the transaction and instructions for further actions.
Web Interface:

Provides a Streamlit interface where users can input transaction details and receive fraud predictions.
Allows users to see if their transaction is flagged as fraudulent and get real-time alerts.

# Screenshots

![pic1_cfd](https://github.com/user-attachments/assets/2e2a20c2-015d-46c1-854f-470598fa5b32)


![pic2_cfd](https://github.com/user-attachments/assets/3df444e1-2c0e-4ebd-bc2a-29c0a5ce9318)



![pic3_cfd](https://github.com/user-attachments/assets/a5010442-a9a6-45ca-87e9-3a0567f7d6cf)


![pic4_cfd](https://github.com/user-attachments/assets/d4a6995a-0ae4-4730-9235-a372a0da09f0)
