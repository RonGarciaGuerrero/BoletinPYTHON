#Autor: Ronald Garcia Guerrero
# 6- Escribir un pequeño programa donde:
#- Se ingresa el año en curso.
#- Se ingresa el nombre y el año de nacimiento de tres personas.
#- Se calcula cuántos años cumplirán durante el año en curso.
#- Se imprime en pantalla.
anio=int(input("Ingrese el año en curso: "))

persona1Nom = input('Para la primera persona, Ingrese el nombre: ')
persona1Anio = input('Para la primera persona, Ingrese el año de nacimiento: ')
persona2Nom = input('Para la segunda persona, Ingrese el nombre: ')
persona2Anio = input('Para la segunda persona, Ingrese el año de nacimiento: ')
persona3Nom = input('Para la tercera persona, Ingrese el nombre: ')
persona3Anio = input('Para la tercera persona, Ingrese el año de nacimiento: ')

def edad(a):
    resp= anio-a
    return resp

print('La edad de '+persona1Nom+' es:'+edad(persona1Anio))