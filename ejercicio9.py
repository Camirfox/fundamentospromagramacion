"""
tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto debera pagar

entrada:
pago

salida:
descuento
"""
pago=input("cual es el pago:" )
pago=int(pago)

prepago=(pago*15)/100
descuento=pago-prepago

print("tu pago final es:",descuento)
