import numpy as np

# Matriu de 4x3 de números aleatoris de 0 a 80
matriu = np.random.randint(0, 80, size=(4,3))

# Leonel
def part1():
    return matriu;

# Mostrem la matriu per pantalla
# print(part1())

# Raul
def part2():
    # Modificar matriz a 3x4
    return matriu.reshape(3,4);
# Mostrem la matriu per pantalla
# print(part2())