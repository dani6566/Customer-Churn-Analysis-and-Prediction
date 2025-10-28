import pandas as pd
from sklearn.model_selection import train_test_split


#Load the dataset from CSV file.
def load_dataset(filepath):
    df = pd.read_csv(filepath)
    return df


def preprocess(df):
    #convert Total Charges to numeric and fill missing values.
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'],errors='coerce')
    df['TotalCharges'].fillna(df['TotalCharges'].median(),inplace = True)
    df.drop(columns = ['customerID'],inplace = True)
    return df

def encode_features(df):
    binary_cols = ['Partner', 'Dependents', 'PhoneService', 'PaperlessBilling', 'Churn']
    for col in binary_cols:
        df[col] = df[col].map({'Yes':1,'No':0})
    df['gender'] = df['gender'].map({'Female':1,'Male':0})
    multi_cols = ['MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
                  'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
                  'Contract', 'PaymentMethod']
    df = pd.get_dummies(df, columns=multi_cols, drop_first=True)
    return df



def split_data(df):
    #Split dataset into training and testing sets.
    X = df.drop('Churn', axis=1)
    y = df['Churn']
    return train_test_split(X, y, test_size=0.2, random_state=42)