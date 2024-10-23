"""
vendedor recibe un sueldo base mas un 10% extra por comision de sus ventas el vendedor desea saber cuanto dinero obtendra por concepto de comisiones 

entradas:
sueldobase, v1, v2, v3, comision
salidas:
monto de comision
pago total
"""
sueldobase=input("ingrese el sueldo base:" )
sueldobase=int(sueldobase)

venta1=input("ingresa la venta 1:" )
venta1=int(venta1)

venta2=input("ingresa la venta 2:" )
venta2=int(venta2)

venta3=input("ingresa la venta 3:" )
venta3=int(venta3)

comision=input("ingresa la comision:" )
comision=int(comision)

comisionT=(venta1 + venta2 + venta3) * 0.10
pagototal=sueldobase+comision

print("el monto de comision es:",comisionT)
print("el pago total es:",pagototal)

