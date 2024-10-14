"""
ejercicio 3:
Programa que calcula la hipotenusa de un triangulo reactangulo a partir de sus catetos
entradas:
cateto1: int
cateto2: int
salidas:
hipotenusa
analisis:
se resuelve con el terorema de pitagoras 
"""
import math
cateto1 = input("escribe el cateto 1:")
cateto1 = int(cateto1)
cateto2 = int(input("escribe el cateto 2:"))
hipotenusa = cateto1 * cateto1 + cateto2 * cateto2
hipotenusa = hipotenusa ** (1/2)
hipotenusa = math.sqrt(hipotenusa)
print("la hipotenusa es:", hipotenusa)
