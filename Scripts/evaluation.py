from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

def plot_roc(model, X_test, y_test):
    """Plot ROC curve and calculate AUC."""
    y_prob = model.predict_proba(X_test)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, label=f'AUC = {roc_auc:.2f}')
    plt.plot([0, 1], [0, 1], 'k--')
    plt.title('ROC Curve')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend()
    plt.show()

def interpret_model(model, feature_names):
    """Print feature importance or coefficients."""
    if hasattr(model, 'coef_'):
        importance = model.coef_[0]
    else:
        importance = model.feature_importances_
    for name, val in zip(feature_names, importance):
        print(f"{name}: {val:.4f}")