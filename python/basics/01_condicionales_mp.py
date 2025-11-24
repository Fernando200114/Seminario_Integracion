"""
Programa para verificar si un pasajero es elegible para reservar un vuelo internacional
Criterios:
- Edad >= 18 años
- Y (tiene pasaporte válido o tiene experiencia previa viajando)
"""

edad = int(input("Edad del pasajero: "))
experiencia = float(input("Años de experiencia viajando: "))
tiene_pasaporte = input("Tiene pasaporte válido (s/n): ").lower() == "s"

# Evaluar elegibilidad
if edad >= 18 and (experiencia >= 1 or tiene_pasaporte):
    print("Elegible para reservar vuelo internacional")
else:
    print("No elegible para reservar vuelo internacional")
