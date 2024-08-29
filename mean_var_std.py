import numpy as np

def calculate(list1):
    b = np.reshape(list1, (3,3))
    calculations = {
        "mean": [list(np.mean(b, axis=0)), list(np.mean(b, axis=1)), np.mean(b)],
        "variance": [list(np.var(b, axis=0)), list(np.var(b, axis=1)), np.var(b)],
        "standard deviation": [list(np.std(b, axis=0)), list(np.std(b, axis=1)), np.std(b)],
        "max": [list(np.max(b, axis=0)), list(np.max(b, axis=1)), np.max(b)],
        "min": [list(np.min(b, axis=0)), list(np.min(b, axis=1)), np.min(b)],
        "sum": [list(np.sum(b, axis=0)), list(np.sum(b, axis=1)), np.sum(b)],
    }
    return calculations