import re

#Este mensage dice "Hola Juan Perez. Tu balance es 53.44$"
nombre = "Juan Perez"
balance = 53.44
print ("Hola %s. Tu balance es %.2f$.\n" % (nombre, balance))

#Esto convierte un string en float
decimal = float("3.14")
print(type(decimal))
print(decimal)
#Esto convierte un float en string
cadena = str(decimal)
print(type(cadena))
print(cadena)
#Esto convierte un float en int (Como es un float, quita los numeros decimales, quedando solo el 3)
entero = int(decimal)
print(type(entero))
print(entero)
#Esto convierte un int en booleano
booleano = bool(1)
print(type(booleano))
print(booleano)

#Esto muestra la longitud de las variables anteriores
print("\nLa longitud de la variable 'decimal' es: ", len([decimal]))
print("La longitud de la variable 'cadena' es: ", len(cadena))
print("La longitud de la variable 'entero' es: ", len([entero]))
print("La longitud de la variable 'booleano' es: ", len([booleano]))

#Método lower(convierte todas las letras en minusculos)
print("\nEl nombre sin lower: ", nombre)
print("El nombre con lower: ", nombre.lower())
#Método upper(convierte todas las letras en mayusculas)
print("\nEl nombre sin upper: ", nombre)
print("El nombre con upper: ", nombre.upper(), "\n")
#Método find(busca una subacadena dentro de una cadena)
msg = "Este es el texto de ejemplo"
print(msg)
print("La posición por la que comienza la palabra 'texto' es: ", msg.find("texto"))
print("Se puede buscar una palabra estableciendo un inicio y un final (comenzando en este desde 'texto' hasta el final): ", msg.find("ejemplo", 11, 27))
print("Si no se encuentra lo que buscas, saldrá un -1 (en este caso la palabra 'casa'): ", msg.find("casa"), "\n")
#Método startwith(sirve para saber si una cadena comienza con una subcadena determinada, retornando 'true' o 'false')
print("\nComo el texto comienza con 'Este' retornará true: ", msg.startswith("Este"))
print("Si ponemos otra palabra que no sea del comienzo retornará false: ", msg.startswith("texto"))
print("Pero si ponemos en donde queremos que comience a buscar podría retornar true (en este caso comenzamos desde la posicion 11 y comprobamos si'texto' es el comienzo):", msg.startswith("texto", 11))
#Método split(parte de una cadena en varias partes, utilizando un separador)
print("\nSe parte la cadena desde 'texto': ", msg.split("texto"))
#Método strip(Elimina los caracteres que se les introduzcan que se encuentran a la izquierda y derecha)
msg2 = "         Esto es otro texto de prueba  "
print("\nEsto es el texto sin quitar los espacios iniciales y finales: ", msg2)
print("Esto es el texto quitando los espacios iniciales y finales que sobran: ", msg2.strip(" "))
#Método index(Comprueba si la subcadena se encuentra en la cadena, devolviendo su posición)
print("\nMuestra la posición de la palabra 'texto' en la cadena 'msg': ", msg.index("texto"))
print("Desde la posición 10 y buscando la misma palabra del mismo mensage muestra la cadena: ", msg.index("texto", 10))
print("Si desde la posición introducida no se encuentra la palabra deseada, dará error\n")

#Esta es la primera frase del "Don Quijote de la Mancha", donde buscaremos el número de veces que sale la letra 'a'
quijote = "«En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor»."
repeticiones = re.search("a", "«En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor».")
print(repeticiones)