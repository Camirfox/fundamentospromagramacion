"""
crea un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde
entradas:total_minutos: int
salidas:
horas:int
minutos:int
"""
total_minutos= input("ingresa la cantidad de minutos:")
total_minutos= int(total_minutos)
horas= (total_minutos // 60)
minutos=(total_minutos%60)
print(f"la cantidad equivale a {horas}horas y {minutos}minutos")
