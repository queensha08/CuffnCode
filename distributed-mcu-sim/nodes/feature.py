import numpy as np

def process(data):
    v, c = data
    power = v * c
    rms = np.sqrt(v**2)
    return v, c, power, rms