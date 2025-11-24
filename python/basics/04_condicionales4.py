"""
Pide cuantos dias registraras
Para cada dia ingresa T(tarde) O(ok) P(permiso)
Cuenta y muestra tardansas totales

"""

dias = int(input("Cuantos dias va a cargar"))
tardes = 0

for i in range(dias):
    marca = input(f"Dia {i+1}T=tarde, O=ok ,P=permiso").strip().upper()
    if marca =="T":
        tardes +=1
        
print(f"tardanzas totales : {tardes}")