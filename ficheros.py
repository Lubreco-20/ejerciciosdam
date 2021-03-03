#Ejercicio 1
print("Escribe un número entre el 1 y el 10")
numero = int(input())
i = 1
if numero >= 1 and numero <= 10:
    f = open("tabla-n.txt", "w")
    for x in range(0, 10):
        resultado = numero * i
        f.write("%d * %d = %d\n" % (numero, i, resultado))
        i += 1
    f.close()
else:
    print("El número está fuera de los límites o no es un número")

#Ejercicio 2
#Escribir un código que pida un número entero entre 1 y 10,
#lea el fichero tabla-n.txt con la tabla de multiplicar de 
#ese número, donde n es el número introducido, y la muestre 
#por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
print("Escribe un número entre el 1 y el 10")
numero = int(input())
i = 1
if numero >= 1 and numero <= 10:
    f = open("tabla-n.txt", "w")
    for x in range(0, 10):
        resultado = numero * i
        f.write("%d * %d = %d\n" % (numero, i, resultado))
        i += 1
    f.close()
    f.open("tabla-n.txt", "r")
    for x in range(0, 10):
        linea = f.readline()
        print(linea)
    f.close()
else:
    print("El número está fuera de los límites o no es un número")