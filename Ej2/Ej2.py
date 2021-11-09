#Autor: Ronald Garcia Guerrero
# 2- Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

a=input('Introduce el primer número: ') 
b=input('Introduce el segundo número: ')
c=input('Introduce el tercer número: ')
def max_de_tres(a,b,c):
    if a>b:
        if a>c:
            result = a
        else:
            if c>b:
                result = c
            else:
                result = b
    else:
        if b>c:
            result=b
        else:
            if c>a:
                result=c
            else:
                result=a
    return result

solucion = max_de_tres(a,b,c)

print ("El numero mayor es :",solucion)
