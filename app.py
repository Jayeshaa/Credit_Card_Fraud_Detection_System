from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import joblib
import matplotlib.pyplot as plt
#import seaborn as sns
import joblib

from twilio.rest import Client

app = Flask(__name__)

#load the trained models
rf_pipeline = joblib.load('rf_pipeline.pkl')
#xgb_pipeline = joblib.load('xgb_pipeline.pkl')
if_pipeline = joblib.load('if_pipeline.pkl')
lof_pipeline = joblib.load('lof_pipeline.pkl')

# Load dataset and fit StandardScaler on it
# data = pd.read_csv('creditcard.csv')
# sc = StandardScaler()
# sc.fit(data[['Time', 'Amount']])

# Twilio credentials 
account_sid = ''
auth_token = ''
twilio_phone_number = ''
user_phone_number = ''
client = Client(account_sid, auth_token)


# Home page route

@app.route('/')

def home():
    return render_template('index.html')

# Route to predict the class of a transaction

@app.route('/predict', methods=['POST'])

def predict():
    data = request.form
    # extract inputs
    time = float(data['Time'])
    amount = float(data['Amount'])

    # Generate additional features if needed
    input_data = pd.DataFrame([[time, amount]], columns=['Time', 'Amount'])

    #predict using the models
    rf_pred = rf_pipeline.predict(input_data)
    #xgb_pred = xgb_pipeline.predict(input_data)
    if_pred = if_pipeline.predict(input_data)
    lof_pred = lof_pipeline.predict(input_data)

    #Determine if fraud or not

    if any(rf_pred == 1) or any(if_pred == -1) or any(lof_pred == -1):
        fraudulent = True
        message_body = "Fraudulent transaction detected!"
    else:
        fraudulent = False
        message_body = "Valid transaction."

    
    # Prepare response
    response = {
        'result': message_body
    }

    return render_template('index.html', prediction=response['result'])

# Send SMS notification if fraudulent
def send_sms(message_body):
    client.messages.create(
        body=message_body,
        from_=twilio_phone_number,
        to=user_phone_number
    )

if __name__ == '__main__':
    app.run(debug=True)


