import logging
from pathlib import Path

import joblib
import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd

from ml.data.preprocessing import DataPreprocessor
from app.config.settings import settings
data_dir = settings.data_dir
data_file = data_dir / "hospital_length_of_stay.csv"

preprocessor = DataPreprocessor()
ARTIFACT_DIR = settings.artifact_dir

logging = settings.get_logger()



from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
    mean_absolute_percentage_error
)

# Linear Models
from sklearn.linear_model import (
    LinearRegression,
    Ridge,
    Lasso,
    ElasticNet,
    BayesianRidge,
    HuberRegressor,
    Lars,
    LassoLars
)

# Tree Models
from sklearn.tree import DecisionTreeRegressor

# Ensemble Models
from sklearn.ensemble import (
    RandomForestRegressor,
    ExtraTreesRegressor,
    GradientBoostingRegressor,
    HistGradientBoostingRegressor,
    AdaBoostRegressor,
    BaggingRegressor
)

# Neighbors
from sklearn.neighbors import KNeighborsRegressor

# External Libraries
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor
from xgboost import XGBRegressor

# =====================================================
# MLFLOW
# =====================================================

mlflow.set_tracking_uri(
    #"http://127.0.0.1/5000"
    "http://localhost:5000"
)

EXPERIMENT_NAME = "Length_Of_Stay"

mlflow.set_experiment(
    EXPERIMENT_NAME
)

# =====================================================
# METRICS
# =====================================================

def evaluate_model(
    y_true,
    y_pred
):

    mae = mean_absolute_error(
        y_true,
        y_pred
    )

    mse = mean_squared_error(
        y_true,
        y_pred
    )

    rmse = np.sqrt(mse)

    r2 = r2_score(
        y_true,
        y_pred
    )

    mape = mean_absolute_percentage_error(
        y_true,
        y_pred
    )

    return {
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse,
        "R2": r2,
        "MAPE": mape
    }


# =====================================================
# DATA
# =====================================================

preprocessor = DataPreprocessor()

df = preprocessor.load_data(
    data_file
)

df = preprocessor.validate_data(df)
df = preprocessor.remove_duplicates(df)
df = preprocessor.feature_engineering(df)

numeric_cols = df.select_dtypes(
    include="number"
).columns.tolist()

numeric_cols.remove(
    "length_of_stay_days"
)

df = preprocessor.cap_outliers(
    df,
    numeric_cols
)

X = df.drop(
    columns=["length_of_stay_days"]
)

y = df["length_of_stay_days"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

X_train = preprocessor.fit_transform(
    X_train
)

X_test = preprocessor.transform(
    X_test
)

feature_names = (
    preprocessor.preprocessor
    .get_feature_names_out()
)

X_train = pd.DataFrame(
    X_train,
    columns=feature_names
)

X_test = pd.DataFrame(
    X_test,
    columns=feature_names
)

preprocessor.save_preprocessor(
    f"{ARTIFACT_DIR}/preprocessor.pkl"
)
# =====================================================
# MODELS
# =====================================================

models = {



    "AdaBoost": AdaBoostRegressor(
        estimator=DecisionTreeRegressor(max_depth=3, random_state=42),
        n_estimators=300,
        learning_rate=0.05,
        loss="square",
        random_state=42,
    ),

    "BayesianRidge":
        BayesianRidge(),

    "DecisionTree":
        DecisionTreeRegressor(
            random_state=42
        ),

    "KNN":
        KNeighborsRegressor(
            n_neighbors=5
        ),

    "Lasso":
        Lasso(
            random_state=42,
            max_iter=10000
        ),

    "ElasticNet":
        ElasticNet(
            random_state=42,
            max_iter=20000
        ),

    "Huber":
        HuberRegressor(),

    "Lars":
        Lars(),

    "LassoLars":
        LassoLars(),

    "RandomForest":
        RandomForestRegressor(
            n_estimators=500,
            random_state=42,
            n_jobs=-1
        ),

    "ExtraTrees":
        ExtraTreesRegressor(
            n_estimators=500,
            random_state=42,
            n_jobs=-1
        ),

    "GradientBoosting":
        GradientBoostingRegressor(
            random_state=42
        ),

    "HistGradientBoosting":
        HistGradientBoostingRegressor(
            random_state=42
        ),

    "Bagging":
        BaggingRegressor(
            random_state=42,
            n_jobs=-1
        ),

    "XGBoost":
        XGBRegressor(
            objective="reg:squarederror",
            random_state=42,
            n_estimators=500
        ),

    "LightGBM":
        LGBMRegressor(
            random_state=42,
            n_estimators=500,
            verbose = -1
        ),

    "CatBoost":
        CatBoostRegressor(
            verbose=False,
            random_state=42,
            iterations=500
        )
}

# =====================================================
# TRAIN ALL MODELS
# =====================================================

results = []

best_r2 = -9999
best_run_id = None
best_model_name = None
print("ML Flow Started")

for model_name, model in models.items():

    with mlflow.start_run(
        run_name=model_name
    ):
        
        model.fit(
            X_train,
            y_train
        )

        y_pred = model.predict(
            X_test
        )

        metrics = evaluate_model(
            y_test,
            y_pred
        )

        mlflow.log_params(
            model.get_params()
        )

        mlflow.log_metrics(
            metrics
        )

        mlflow.sklearn.log_model(
            sk_model=model,
            name="model",
            serialization_format="cloudpickle",
        )

        results.append({
            "Model": model_name,
            **metrics
        })

        print(
            f"{model_name} R2={metrics['R2']:.4f}"
        )

        if metrics["R2"] > best_r2:

            best_r2 = metrics["R2"]
            best_model = model

            best_run_id = (
                mlflow.active_run().info.run_id
            )

            best_model_name = model_name

            
            

print("ML Flow Completed")

# =====================================================
# RESULTS
# =====================================================

results_df = pd.DataFrame(
    results
).sort_values(
    by="R2",
    ascending=False
)

print("\n")
print(results_df)

results_df.to_csv(
    f"{ARTIFACT_DIR}/regression_results.csv",
    index=False
)

print("\nBest Model:", best_model_name)
print("Best R2:", best_r2)
print("Run ID:", best_run_id)

# =====================================================
# REGISTER BEST MODEL
# =====================================================

model_uri = (
    f"runs:/{best_run_id}/model"
)

registered_model_name = (
    "LengthOfStayRegressor"
)

registered_model = mlflow.register_model(
    model_uri=model_uri,
    name=registered_model_name
)

print(
    f"Registered Model: "
    f"{registered_model_name}"
)

print(
    f"Version: "
    f"{registered_model.version}"
)

# Canonical artifact consumed by ModelLoader.
best_model_path = ARTIFACT_DIR / "best_model.pkl"
joblib.dump(best_model, best_model_path)

# Keep a descriptive copy for inspection / manual selection.
named_model_path = ARTIFACT_DIR / f"{best_model_name}.pkl"
joblib.dump(best_model, named_model_path)

print(f"Best model saved as: {best_model_path}")
print(f"Named model copy saved as: {named_model_path}")