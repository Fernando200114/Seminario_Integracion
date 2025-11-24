"""
Escribe un programa que pidad edad, años de experiencia y sio tiene el titulo universitario
un candidato es elegible si tiene >=21 años y experiencia >= 2 años o titulo
Muestra elegible o no elegible 
"""

edad = int(input("Edad del candidato :"))
exp = float(input("Años de experiencia: "))
tiene_titulo = input("tiene titulo unioversitario s/n:").lower()=="s"

if (edad >=21 and (exp>=2 or tiene_titulo=="s")):
    print("Elegible")
else:
    print("No Elegible")