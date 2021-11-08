#Autor: Ronald Garcia Guerrero
# 5- Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
def suma(a):
    total = 0
    for i in range(len(a)):
        total += a[i] 
    return total
def mult(a):
    total = 1
    for i in range(len(a)):
        total *= a[i]
    return total


lista=[1,2,3,4,5] #me obliga a inicializar la lista 1,2,3,4,5

print('La sumatoria de los elementos de la lista es: ',suma(lista))


print('La multiplicacion de los elementos de la lista es: ',mult(lista))
print('Hasta luego!')