import pandas as pd

def segment_customers(df):
    """Segment customers by tenure, monthly charges, and contract type."""
    df['TenureGroup'] = pd.cut(df['tenure'], bins=[0, 12, 24, 48, 72], labels=['0-12', '13-24', '25-48', '49-72'])
    df['ChargeGroup'] = pd.cut(df['MonthlyCharges'], bins=[0, 40, 80, 120], labels=['Low', 'Medium', 'High'])
    return df

def churn_by_segment(df):
    """Analyze churn within segments."""
    segment_cols = ['TenureGroup', 'ChargeGroup', 'Contract']
    for col in segment_cols:
        churn_rate = df.groupby(col)['Churn'].mean()
        print(f"Churn rate by {col}:\n", churn_rate)

def identify_high_value_risk(df):
    """Identify high-value customers at risk of churn."""
    high_value = df[(df['ChargeGroup'] == 'High') & (df['Churn'] == 1)]
    return high_value[['tenure', 'MonthlyCharges', 'Contract']]