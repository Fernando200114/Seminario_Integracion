"""
Sistema que pida el pago por hora y horas trabajadas
Las primeras 40h son normales, las extras se les paga el 150%
Calcula y muestra el total semanal

"""

pago_horas = int(input("Ingrese el pago por horas :"))
horas_trabajadas = int(input("Ingrese las horas trabajadas:"))



if horas_trabajadas <= 40:
    extras = horas_trabajadas * pago_horas


else: 
    horas = horas_trabajadas - 40
    extras = (pago_horas * 40) + (pago_horas  * 1.5 * horas)
    
print(f"El valor total es de : {extras:.1f}")
    