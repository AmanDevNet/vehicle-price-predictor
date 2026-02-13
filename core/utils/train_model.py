
import os
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.pipeline import Pipeline
import logging
from core.utils.data_ingestion import fetch_data
from core.utils.data_cleaning import clean_data

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MODEL_PATH = "model.pkl"

def train_and_save_model(model_path: str = MODEL_PATH):
    """
    Fetches data, cleans it, trains a Random Forest model, and saves the pipeline.
    """
    try:
        # Load data
        df = fetch_data()
        
        # Clean and split
        X_train, X_test, y_train, y_test, preprocessor = clean_data(df)
        
        # Create full pipeline with model
        model = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
        ])
        
        # Train
        logger.info("Training model...")
        model.fit(X_train, y_train)
        
        # Evaluate
        y_pred = model.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        logger.info(f"Model trained. MAE: {mae:.2f}, R2 Score: {r2:.2f}")
        
        # Save
        joblib.dump(model, model_path)
        logger.info(f"Model saved to {model_path}")
        
    except Exception as e:
        logger.error(f"Error during training: {e}")
        raise

if __name__ == "__main__":
    train_and_save_model()
