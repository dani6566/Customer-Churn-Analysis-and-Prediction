from Scripts.load_data import load_dataset,preprocess,encode_features,split_data
from Scripts.EDA import plot_churn_rate,plot_demographics,plot_contract_payment,plot_tenure_churn
from Scripts.segmentation import segment_customers,churn_by_segment,identify_high_value_risk
from Scripts.modeling import train_models,evaluate_models
from Scripts.evaluation import plot_roc,interpret_model
from Scripts.recommendations import estimate_impact,generate_recommendations,print_recommendations


#Load and prepare data
df = load_dataset("./Data/Telco_Customer_Churn_Dataset.csv")
print(df.head(5))
prep_df = preprocess(df)

#EDA
plot_churn_rate(prep_df)
plot_demographics(prep_df)
plot_contract_payment(prep_df)
plot_tenure_churn(prep_df)

#split data for train and test
encode_df = encode_features(prep_df)
print(encode_df)
X_train,X_test,y_train,y_test = split_data(encode_df)

#Customer Segmentaion
df_segmented = segment_customers(df)
churn_by_segment(df)
high_value_risk = identify_high_value_risk(df_segmented)
print("High-value customers at risk:\n",high_value_risk.head())

#model Training and evaluation
log_model,tree_model = train_models(X_train, y_train)
models = {"logistic Regression":log_model,"Decision Tree":tree_model}
evaluate_models(models,X_test, y_test)

#Model Interpretation
plot_roc(log_model,X_test,y_test)
interpret_model(log_model,X_train.columns)

#  Business Recommendations
print_recommendations()
estimate_impact(df_segmented)






