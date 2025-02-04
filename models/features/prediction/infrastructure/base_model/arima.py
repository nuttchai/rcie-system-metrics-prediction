import time
import pandas as pd
from typing import Any
from statsmodels.tsa.arima.model import ARIMA as ARIMAM
from interface import IBaseModel


class ARIMA(IBaseModel):
    def __init__(self):
        self.dataset = None
        self.training_dataset = None
        self.model = None

    def PrepareParameters(
        self,
        dataset: pd.DataFrame,
        feature: str,
        start_index: int,
        end_index: int,
    ):
        # Copy dataset to avoid changing the original dataset
        cp_dataset = dataset.copy()
        # Set up configuration
        self.dataset = cp_dataset[feature]
        self.training_dataset = (
            self.dataset.iloc[start_index:]
            if end_index is None
            else self.dataset.iloc[start_index:end_index]
        )

    def TrainModel(self, config: dict) -> Any:
        """
        Train an ARIMA model on a given time series.
        - series: Pandas Series object representing the time series data.
        - order: A tuple representing the (p,d,q) parameters for ARIMA.
        """
        start_time = time.time()
        order = config.get("order", None)
        model = ARIMAM(self.training_dataset, order=order)
        self.model = model.fit()
        end_time = time.time()
        print(f"[ARIMA] Training time: {end_time - start_time} seconds")
        return self.model

    def Predict(self, config: dict) -> pd.DataFrame:
        # Add timer for prediction
        start_time = time.time()
        steps = config.get("steps", 1)
        predicted = self.model.forecast(steps=steps)
        end_time = time.time()
        print(f"[ARIMA] Prediction time: {end_time - start_time} seconds")
        return predicted

    def SaveModel(self, model: Any):
        self.model = model
