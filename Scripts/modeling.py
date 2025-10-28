from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def train_models(X_train, y_train):
    """Train logistic regression and decision tree models."""
    log_model = LogisticRegression(max_iter=1000)
    tree_model = DecisionTreeClassifier(max_depth=5)
    log_model.fit(X_train, y_train)
    tree_model.fit(X_train, y_train)
    return log_model, tree_model

def evaluate_models(models, X_test, y_test):
    """Evaluate models using classification metrics."""
    for name, model in models.items():
        y_pred = model.predict(X_test)
        print(f"{name} Accuracy: {accuracy_score(y_test, y_pred):.2f}")
        print(f"{name} Precision: {precision_score(y_test, y_pred):.2f}")
        print(f"{name} Recall: {recall_score(y_test, y_pred):.2f}")
        print(f"{name} F1 Score: {f1_score(y_test, y_pred):.2f}")