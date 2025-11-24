"""
Vacaciones por antiguedad 
Pide años de antiguedad y muestra los dias de vacaciones segun
<1 = 0
<3 = 3
<5 = 10
>=5 = 15
"""

print("Sistema de vacaciones")

años_antiguedad = int(input("Por favor ingresa los primeros años de trtabajo"))

if años_antiguedad <1 :
    print("No tiene dias de vacaciones")
elif años_antiguedad <3:
    print("Tienes tres dias de vacaciones")
elif años_antiguedad <5:
    print("tiene 10 dias de vacaciones")
else:
    años_antiguedad >=5
    print("Tiene 15 dias de vacciones ") 