import numpy as np

def ndarray():
  # Creem una matriu de zeros de dimensions 50x50
  matriu = np.zeros((50,50))

  # Omplim la diagonal amb números ascendents des de 0 a 49
  for i in range(50):
    matriu[i,i] = i

  return matriu

# Cridem la funció i mostrem per pantalla el resultat
#print(ndarray())
