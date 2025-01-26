
import pandas as pd
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, accuracy_score

def load_data(file_path):
    data = pd.read_csv(file_path)
    X = data.drop(columns=['tornado'])
    y = data['tornado']
    return X, y

def train_model(X, y):
    model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    model.fit(X, y)
    return model

def optimize_model(X, y):
    param_dist = {
        'n_estimators': [50, 100, 200],
        'learning_rate': [0.01, 0.1, 0.2],
        'max_depth': [3, 5, 7],
        'subsample': [0.8, 1.0],
        'colsample_bytree': [0.8, 1.0]
    }
    model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    random_search = RandomizedSearchCV(model, param_dist, n_iter=50, cv=3, scoring='accuracy', verbose=2)
    random_search.fit(X, y)
    return random_search.best_estimator_

def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print("=== Report di Valutazione ===")
    print(classification_report(y_test, predictions))
    print(f"Accuratezza del modello: {accuracy}")
    return accuracy

if __name__ == "__main__":
    X, y = load_data("updated_dataset.csv")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = optimize_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
