# Un analista financiero lleva un registro del precio del dólar día a día,
#  y desea saber cuál fue la mayor de las alzas en el precio diario a lo largo de ese período.
# Escriba un programa que pida al usuario ingresar el número n de días, y 
# luego el precio del dólar para cada uno de los n días.
# El programa debe entregar como salida cuál fue la mayor de las alzas de
#  un día para el otro.
# Si en ningún día el precio subió, la salida debe decir: No hubo alzas.

alzaDolar = []
valorDolarDia = []

numeroDias = int(input("Ingrese el numero de dias a evaluar \n"))
print("Ingrese el valor de cada dia a evaluar")
for i in range(1, numeroDias+1):
    precioDolarDiaADia = int(input(f"Vaolor Dia {i}: "))
    valorDolarDia.append(precioDolarDiaADia)

for i in range(1, numeroDias-1):
    valorAlzaDolar = valorDolarDia[i+1]-valorDolarDia[i]
    if valorDolarDia[i+1] == valorDolarDia[i]:
        print(f"No hubo alzas el dia {i+2}")
    alzaDolar.append(valorAlzaDolar)

valorAlzaMayor = max(alzaDolar)
print(f"El valor del alza mayor fue {valorAlzaMayor}")