# models/anomaly_detection.py
from sklearn.ensemble import IsolationForest
import numpy as np

def detect_anomalies(movement_data):
    """
    Uses Isolation Forest to detect anomalies in movement.
    :param movement_data: numpy array of movement vectors
    :return: array of predictions, where -1 indicates an anomaly
    """
    clf = IsolationForest(random_state=42).fit(movement_data)
    predictions = clf.predict(movement_data)
    return predictions
