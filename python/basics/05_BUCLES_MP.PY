"""
Calcula la nómina total de tripulantes
- Pide el número de tripulantes
- Luego pide el salario de cada uno
- Muestra la nómina total
"""

num_tripulantes = int(input("Ingrese el número de tripulantes: "))
nomina_total = 0

for i in range(num_tripulantes):
    salario = float(input(f"Ingrese el salario del tripulante {i+1}: "))
    nomina_total += salario

print(f"La nómina total de los tripulantes es: ${nomina_total:.2f}")
