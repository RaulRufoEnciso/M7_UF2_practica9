import exercici1 as ex1
import exercici2 as ex2
import exercici3 as ex3
# LEONEL RUIZ
print("Mostra en una matriz donde solo se quieren numeros ascendentes en la diagonal de '0 a 49'")
print(ex1.ndarray())

# RAUL RUFO
print("Ejercicio 2")
print("Array eje0:")
print(ex2.part1())
print("Array eje1:")
print(ex2.part2())
print("Array con reshape(4,1):")
print(ex2.part3())

#Javier
print('Dame tres numeros')
x, y, z = input(), input(), input()
print('Devolveremos valores enteros aleatorios de los valores especificados con parámetro bajo (inclusivo) a  alto  (exclusivo).')
print(ex3.generaRandom(x,y,z))
print('Dame tres numeros')
a, b, c = input(), input(), input()
print('Devolvemos el maximo valor de array')
print(ex3.valorMaximo(a,b,c))
print('Dame tres numeros')
d, e, f = input(), input(), input()
print('Devolvemos el minimo valor de array')
print(ex3.valorMinimo(d,e,f))