import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    arr = np.array(x)
    arr = np.where(arr < 0, arr * alpha, arr)
    return arr