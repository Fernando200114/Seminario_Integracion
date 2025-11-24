"""
Pide salario y clasifica el cargo
<1000 junior
1000-2000 semi senior
>2000 senior
"""


salario = int(input("Ingrese el salario"))

if salario <1000:
    print("junior")
elif 1000 <= salario <= 2000:
    print("Es semi senior")
else:
    salario > 2000
    print("Senior")
    