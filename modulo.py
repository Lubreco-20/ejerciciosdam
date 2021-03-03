#Módulo del ejercicio 1
def elementos(texto):
    textoDividido = texto.split(" ")
    principio = textoDividido[0]
    final = textoDividido[-1]

    print("Inicio: %s; Final %s" % (principio, final))

#Módulo del ejercicio 2
def sumaElementos(lista):
    final = 0
    for numero in lista:
        final += numero
    print("Y esta es la lista sumada")
    return final