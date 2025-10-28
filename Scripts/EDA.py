import matplotlib.pyplot as plt
import seaborn as sns


def plot_churn_rate(df):
    #Plot overall churn rate.
    churn_rate = df['Churn'].value_counts(normalize = True)
    churn_rate.plot(kind='bar',title="Churn Rate")
    plt.show()


def plot_demographics(df):
  #Visualize churn by gender, partner, and dependents.
    for col in ['gender', 'Partner', 'Dependents']:
        sns.countplot(x=col, hue='Churn', data=df)
        plt.title(f'Churn by {col}')
        plt.show()

def plot_tenure_churn(df):
  #Analyze tenure distribution and churn.
    sns.histplot(data=df, x='tenure', hue='Churn', bins=30, kde=True)
    plt.title('Tenure Distribution by Churn')
    plt.show()

def plot_contract_payment(df):
  #Visualize churn by contract type and payment method.
    for col in ['Contract', 'PaymentMethod']:
        sns.countplot(x=col, hue='Churn', data=df)
        plt.xticks(rotation=45)
        plt.title(f'Churn by {col}')
        plt.show()