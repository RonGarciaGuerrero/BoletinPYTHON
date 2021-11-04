# 4- Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
char = input('Introduce un caracter: ')
vocales ="aeiou" 
#declaro una variable tipo cadena que incluya todas las vocales
def miCar(a):
#declaro una función para buscar el caracter pasado por teclado en la cadena de vocales, uso la funcion string.find("valorABuscar"), si devuelve -1 es que no la ha encontrado y es una consonante
    if (vocales.find(a)<0):
        b='= False, es una consonante.'
    else:
        b='= True, es una vocal.'
    return b
resp=miCar(char)
print('Para el caracter :',char,resp)