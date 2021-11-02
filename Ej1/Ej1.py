# 1- Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

a=input('Introduce el primer número: ') 
b=input('Introduce el primer número: ')
def esMayor(a,b):
    if a>b:
        result = a
    else:
        result=b
    return result

solucion = esMayor(a,b)

print ("El numero mayor es :",solucion)
