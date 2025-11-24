"""
Pide el numero de empleados y luego el sueldo d cada uno
suma y muestra la nomina totalñ

"""


empleados= int(input("ingrese el numero de empleados :"))
nomina = 0



for val in range(empleados):
    sueldo = float(input("Ingrese el sueldo " ))
    nomina += sueldo
    
print(f"El sueldo es de {nomina}")