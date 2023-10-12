import os
import sys

# Add path to the root folder
sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    )
)
from pconstant.models_id import ARIMA, ETS, LSTM

# NOTE: Define the selected feature to be predicted here
# FEATURES = ["cpu_usage", "memory_usage", "bandwidth_inbound", "bandwidth_outbound", "tps", "response_time"]
SELECTED_FEATURE = "cpu_usage"

# NOTE: Define the number of steps to be predicted here
PREDICTION_STEPS = 2

# NOTE: Define the number of recreation model steps here (not used yet)
RECREATION_MODEL_STEPS = 2  # Should be time interval

# NOTE: Define the number of initial base training size here
INITIAL_BASE_TRAINING_SIZE = 1000

# NOTE: Define the number of initial meta training size here
INITIAL_META_TRAINING_SIZE = 100

# NOTE: Use filter (reduce noise) or not
IS_FILTERED = True

# NOTE: Define the default setup configuration (hyperparameter) of each model here
SETUP_ARIMA_CONFIG = {"order": (1, 1, 1)}
SETUP_ETS_CONFIG = {
    "trend": "add",
    "seasonal": "add",
    "seasonal_periods": 12,
}  # 12 -> 12 * 5 seconds = 1 minute
SETUP_PROPHET_CONFIG = {}
SETUP_LSTM_CONFIG = {
    "seq_length": 10,
    "steps": PREDICTION_STEPS,
    "epochs": 3,
    "verbose": 0,  # 0: silent, 1: progress bar, 2: one line per epoch
}

# NOTE: Define the default prediction configuration of each model here
PREDICTION_ARIMA_CONFIG = {}
PREDICTION_ETS_CONFIG = {}
PREDICTION_PROPHET_CONFIG = {}
PREDICTION_LSTM_CONFIG = {
    "seq_length": SETUP_LSTM_CONFIG.get("seq_length", 10),
    "steps": SETUP_LSTM_CONFIG.get("steps", PREDICTION_STEPS),
    "verbose": 0,  # 0: silent, 1: progress bar, 2: one line per epoch
}


# NOTE: Define the list of base model ids here
BASE_MODELS_IDS = [ARIMA, ETS, LSTM]

# NOTE: Define the list of meta model ids here
META_MODELS_IDS = []
