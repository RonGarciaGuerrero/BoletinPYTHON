# 5- Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
#Defino las funciones para sumar y multiplicar
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

#Para definir cuantos elementos va a tener la lista lo pregunto por input al usuario
longitud = int(input('Introduce un número de elementos que va a tener la lista: '))-1
lista=[] #inicializo la lista
#ahora itero pidiendo los numeros que va a tener la lista
for i in range(longitud+1):
    lista.append(int(input('Introduce un número para ir rellenando la lista: ')))

#ahora imprimo llamando a las funciones
print('La sumatoria de los elementos de la lista es: ',suma(lista))

print('La multiplicacion de los elementos de la lista es: ',mult(lista))

print('Hasta luego!')
