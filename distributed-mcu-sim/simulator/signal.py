import numpy as np

def generate_signal():
    voltage = 220 + np.random.randn() * 8
    current = 1 + np.random.randn() * 0.25
    return voltage, current