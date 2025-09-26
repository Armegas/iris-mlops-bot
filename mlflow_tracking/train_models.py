from prefect import flow, task
import mlflow
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
import pickle

@task
def load_data():
    X, y = load_iris(return_X_y=True)
    return X, y

@task
def split_data(X, y):
    return train_test_split(X, y, test_size=0.2)

@task
def train_and_log_models(X_train, X_test, y_train, y_test):
    models = {
        "LogisticRegression": LogisticRegression(),
        "DecisionTree": DecisionTreeClassifier(max_depth=3),
        "XGBoost": XGBClassifier(n_estimators=50)
    }
    scores = {}
    for name, model in models.items():
        with mlflow.start_run(run_name=name):
            model.fit(X_train, y_train)
            preds = model.predict(X_test)
            acc = accuracy_score(y_test, preds)
            mlflow.log_param("model", name)
            mlflow.log_metric("accuracy", acc)
            mlflow.sklearn.log_model(model, "model")
            scores[name] = acc
    return models, scores

@task
def save_best_model(models, scores):
    best_name = max(scores, key=scores.get)
    best_model = models[best_name]
    with open("models/trained_model.pkl", "wb") as f:
        pickle.dump(best_model, f)
    return best_name

@flow(name="iris_flow")
def iris_pipeline():
    X, y = load_data()
    X_train, X_test, y_train, y_test = split_data(X, y)
    models, scores = train_and_log_models(X_train, X_test, y_train, y_test)
    best = save_best_model(models, scores)
    print(f"Best model: {best}")

if __name__ == "__main__":
    iris_pipeline()