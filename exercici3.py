import random
import numpy as np

def generaRandom(x, y, z):
    aRandomDiez = np.random.randint(low=x, high=y, size=z)
    return aRandomDiez

def valorMaximo(x, y, z):
    aRandomDiez = np.random.randint(low=x, high=y, size=z)
    return np.amax(aRandomDiez)

def valorMinimo(x, y, z):
    aRandomDiez = np.random.randint(low=x, high=y, size=z)
    return np.amin(aRandomDiez)


print(generaRandom(0, 100, 100))
print(valorMaximo(0, 100, 100))
print(valorMinimo(0, 100, 100))
