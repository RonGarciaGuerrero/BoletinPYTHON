#Autor: Ronald Garcia Guerrero
# 6- Escribir un pequeño programa donde:
#- Se ingresa el año en curso.
#- Se ingresa el nombre y el año de nacimiento de tres personas.
#- Se calcula cuántos años cumplirán durante el año en curso.
#- Se imprime en pantalla.

#Primero defino la función de calcular la edad
def edad(a):
    resp= anio-a
    return resp
#pido el año actual
anio=int(input("Ingrese el año en curso: "))
#uso listas para almacenar los nombres y los años de nacimiento
nombres=[]
anioNac=[]

#itero 3 veces y guardo los datos en la lista
print('A continuación se pedira que introduzca nombres de personas y sus años de nacimiento.')
for i in range(3):
    nombres.append(input('Ingrese un nombre: '))
    anioNac.append(int(input('Ingrese su año de nacimiento: ')))

#itero 3 veces para imprimir llamando a la lista y a la función de edad
for i in range(3):
    print('La edad de ',nombres[i]+' es: ',edad(anioNac[i]))
print('Fin')
