# 5- Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
#De esta manera no consegui hacerlo
def sum():
    resultado=0 #acumulador
    for i in range(longitud):
        resultado=lista[i]+lista[i+1]
    return resultado

def multip():
    resultado=1 #acumulador 
    for i in range(longitud):
        resultado=lista[i]*lista[i+1]
    return resultado


longitud = int(input('Introduce un número de elementos que va a tener la lista: '))-1
lista=[] #me obliga a inicializar la lista
#print(longitud)
i=0
#longitud=len(lista)
for i in range(longitud):
    lista.append(int(input('Introduce un número para ir rellenando la lista: ')))

opcion = int(input('Para usar la funcion de sumar introduzca 1 para multiplicar 2, para salir cualquier otro valor: '))
if opcion==1:
    print('La sumatoria de los elementos de la lista es: ',sum(lista))

if opcion==2:
    print('La multiplicacion de los elementos de la lista es: ',resultado)
else:
    print('Hasta luego!')
