import numpy as np

def rmse(predictions, targets):
    pred = np.array(predictions)
    tar = np.array(targets)
    rmse = np.sqrt(np.mean(np.square((tar - pred))))
    return rmse