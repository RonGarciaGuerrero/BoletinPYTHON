# 4- Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
char = input('Introduce un caracter: ')
vocales ="aeiou"
def miCar(a):
    if (vocales.find(a)<0):
        b='False, es una consonante'
    else:
        b='True, es una vocal'
    return b
resp=miCar(char)
print(char,resp)