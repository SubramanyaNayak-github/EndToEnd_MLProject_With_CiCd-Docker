import joblib 
import numpy as np
import pandas as pd
from pathlib import Path

    
class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))
        self.scaler = joblib.load(Path('artifacts/data_transformation/scaler.joblib'))

    def preprocess_data(self, data):
        scaled_data = pd.DataFrame(self.scaler.transform(data), columns=data.columns)
        return scaled_data

    def predict(self, data):
        scaled_data = self.preprocess_data(data)
        prediction = self.model.predict(scaled_data)
        return prediction