import random
import numpy as np

def generaRandom(x, y, z):
    aRandomDiez = np.random.randint(low=x, high=y, size=z)
    return aRandomDiez

print(generaRandom(0,100, 100))