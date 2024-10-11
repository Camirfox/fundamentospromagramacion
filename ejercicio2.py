"""
programa 2:
Crear un programa que calcule area y perimetro de un rectangulo
Entradas:
dase: integer
altura: integer
salidas:
area: integer
perimetro: integer
"""
base= input("ingresa la base ")
base= int(base)
altura= input("ingresa la altura")
altura= int(altura)
area= (base * altura) * 2
perimetro= (base * altura) * 2
print("el area del rectangulo es", area)
print("el perimetro del rectangulo es", perimetro)