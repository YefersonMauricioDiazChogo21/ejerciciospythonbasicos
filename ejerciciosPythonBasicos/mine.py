# Crear una lista de numeros aleatorios e imprimir la lista original
# la lista de manera ascendente y de manera descendente
import random
listaOriginal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, 11):
    listaOriginal[0] = random.randint(1,11)
print(f"Lista original: {listaOriginal}")

listaAscendente =  sorted(listaOriginal)
print(f"Lista ascendente: {listaAscendente}")

listaDescendente = sorted(listaOriginal, reverse = True)
print(f"Lista descendente: {listaDescendente}")