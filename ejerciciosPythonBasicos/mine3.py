# Una máquina de alimentos tiene productos de tres tipos,
# A, B y C, que valen respectivamente $270, $340 y $390. 
# La máquina acepta y da de vuelto monedas de $10, $50 y $100.

# Escriba un programa que pida al usuario elegir el producto 
# y luego le pida ingresar las monedas hasta alcanzar el monto 
# a pagar. Si el monto ingresado es mayor que el precio del producto,
# el programa debe entregar las monedas de vuelto, una por una.

print("Ingrese el numero del producto que desea comprar")
productoElegido =int(input("\t 0. A     $270\n\t 1. B     $340\n\t 2. C     $390\n Producto N°: "))
valorProducto=0

if productoElegido == 0:
    valorProducto = valorProducto +270
elif productoElegido ==1:
    valorProducto = valorProducto +340
elif productoElegido == 2:
    valorProducto = valorProducto +390

valorTotalIngresado = 0
while valorProducto>valorTotalIngresado:
    monedaIngresada =int(input("\tIngrese monedas para el pago, recuerde\n\tsolo aceptamos monedas de 100, 50 y 10\n\t - "))
    valorTotalIngresado = valorTotalIngresado+monedaIngresada 
    valorCambio = valorTotalIngresado-valorProducto
print("Entregando su cambio")
while valorCambio!=0:
    if valorCambio>100:
        print("\t100")
        valorCambio = valorCambio-100
    elif valorCambio>50:
        valorCambio = valorCambio-50
        print("\t50")
    else:
        print("\t10")
        valorCambio = valorCambio-10