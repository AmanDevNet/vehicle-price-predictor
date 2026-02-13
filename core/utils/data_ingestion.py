
import pandas as pd
import requests
import io
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATA_URL = "https://raw.githubusercontent.com/ShuklaPrashant21/Used-Car-Price-Prediction/master/car%20data.csv"

def fetch_data(url: str = DATA_URL) -> pd.DataFrame:
    """
    Fetches data from the given URL and returns a pandas DataFrame.
    """
    try:
        logger.info(f"Fetching data from {url}...")
        response = requests.get(url)
        response.raise_for_status()
        content = response.content
        df = pd.read_csv(io.BytesIO(content))
        logger.info(f"Data fetched successfully. Shape: {df.shape}")
        return df
    except Exception as e:
        logger.error(f"Error fetching data: {e}")
        raise
