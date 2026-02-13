
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import logging

logger = logging.getLogger(__name__)

def clean_data(df: pd.DataFrame):
    """
    Cleans and preprocesses the dataframe.
    Returns X_train, X_test, y_train, y_test, and the preprocessor pipeline.
    """
    logger.info("Cleaning data...")
    
    # Drop Car_Name as it has high cardinality and might not be useful for this generalized model
    if 'Car_Name' in df.columns:
        df = df.drop(columns=['Car_Name'])
    
    # Separate features and target
    X = df.drop(columns=['Selling_Price'], errors='ignore')
    y = df['Selling_Price']
    
    # Identify categorical and numerical columns
    categorical_cols = ['Fuel_Type', 'Seller_Type', 'Transmission']
    numerical_cols = ['Year', 'Present_Price', 'Kms_Driven', 'Owner']
    
    # Create preprocessing steps
    numerical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])
    
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown='ignore'))
    ])
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_cols),
            ('cat', categorical_transformer, categorical_cols)
        ]
    )
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    logger.info("Data cleaned and split.")
    return X_train, X_test, y_train, y_test, preprocessor
