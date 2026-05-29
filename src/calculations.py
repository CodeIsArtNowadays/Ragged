import numpy as np


def l2_norm(v):
    return np.sqrt(np.sum(np.square(v)))

def cos_sim(v1, v2):
    return np.dot(v1, v2) / (l2_norm(v1) * l2_norm(v2))
