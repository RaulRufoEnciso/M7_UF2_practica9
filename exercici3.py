import random
import numpy as np

def generaRandom(x, y, z):
    aRandomDiez = np.random.randint(low=x, high=y, size=z)
    return aRandomDiez

def valorMaximo(a, b, c):
    aRandomDiez = np.random.randint(low=a, high=b, size=c)
    return np.amax(aRandomDiez)

def valorMinimo(d, e, f):
    aRandomDiez = np.random.randint(low=d, high=e, size=f)
    return np.amin(aRandomDiez)


print(generaRandom(0, 100, 100))
print(valorMaximo(0, 100, 100))
print(valorMinimo(0, 100, 100))
