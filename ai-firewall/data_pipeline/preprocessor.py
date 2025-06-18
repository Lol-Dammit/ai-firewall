# data_pipeline/preprocessor.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

def preprocess(features: list[dict]) -> np.ndarray:
    """
    Takes list of parsed packets and returns scaled numerical data.
    """
    df = pd.DataFrame(features)
    df.fillna(0, inplace=True)

    numerical_features = df[["length"]]
    scaled = scaler.fit_transform(numerical_features)
    return scaled
