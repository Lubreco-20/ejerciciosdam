#Ejercicio 1
#Print i as long as i is less than 6.
i = 1
while i < 6:
  print(i)
  i += 1

#Stop the loop if i is 3.
i = 1
while i < 6:
  if i == 3:
    break
  i += 1

#In the loop, when i is 3, jump directly to the next iteration.
i = 0
while i < 6:
  i += 1
  if i == 3:   
    continue
  print(i)

#Print a message once the condition is false.
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#Ejercicio 2
print("Introduce un número")
numero = int(input())
while numero > 0:
  print(numero)
  numero-=1
else:
  print("Fin del número")

#Ejercicio 3
print("Introduce un número")
numero = int(input())
while numero > 0:
  if numero%2 != 0:
    print(numero)
  numero-=1

#Ejercicio 4
print("Comencemos con el eco")
eco = ""
while eco != "salir":
  eco = input()
  i = 1
  while i < 3:
    print(eco)
    i += 1

#Ejercicio 5
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
i = 0
while(i < len(asignaturas)):
  print("¿Que has sacado en %s?" % (asignaturas[i]))
  nota = input()
  notas.append(nota)
  i += 1

i = 0
while(i < len(asignaturas)):
  print("En %s, has sacado %s" % (asignaturas[i], notas[i]))
  i += 1

#Ejercicio 6
boletos = []
print("¿Cuántos boletos quieres?")
cantidad = int(input())
i = 0
while(i < cantidad):
  boleto = input("Nº boleto: ")
  boletos.append(boleto)
  i += 1

print(sorted(boletos))

#Ejercicio 7
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
borrar = []
i = 0
while(i < len(asignaturas)):
  print("¿Que has sacado en %s?" % (asignaturas[i]))
  nota = int(input())
  notas.append(nota)
  i += 1

i = 0
while(i < len(asignaturas)):
  if notas[i] < 5:
    borrar.append(asignaturas[i])
  i += 1

print("Tiene que repetir las asignatura %s" % (borrar))
cantidad = len(borrar)
i = 0
while i < cantidad:
  asignaturas.remove(borrar[i])
  i += 1

#Ejercicio 8
print("Introduce un texto para ver si es un palindromo")
texto = input()
if str(texto) == str(texto)[::-1]:
  print("Es palindroma")
else:
  print("No es palindroma")

#Ejercicio 9
print("Introduce un texto para saber cuantas vocales tiene")
cadena = str(input())
A = 0
E = 0
I = 0
O = 0
U = 0
for letra in cadena:
  if letra.lower() in "e":
    E += 1
  if letra.lower() in "i":
    I += 1
  if letra.lower() in "o":
    O += 1
  if letra.lower() in "u":
    U += 1
  if letra.lower() in "a":
    A += 1

print("El texto tiene: %d A, %d E, %d I, %d O y %d U" % (A,E,I,O,U))

#Ejercicio 10
print("Escribe una palabra y luego su traducción al inglés")
print("Escriba salir para dejar de introducir palabras")
español = []
ingles = []
final = []
palabras = str(input("Español: "))
while palabras != "salir":
  traduccion = str(input("Inglés: "))
  print(palabras + ":" + traduccion)
  español.append(palabras)
  ingles.append(traduccion)
  palabras = str(input("Español: "))

print("Ahora escribe una frase para que se traduzca")
texto = str(input())
x = texto.split(" ")
i = 0
while i < len(x):
  palabra = x[i]
  if palabra in español:
    posicion = español.index(palabra)
    word = ingles[posicion]
    final.append(word)
  else:
    final.append(palabra)
  i += 1  

listo = " ".join(final)
print(listo)

#Ejercicio 11
print("Bienvenido a la gestión de facturas")
opcion = ""
cod = []
cost = []
while (opcion != 3):
    print("====================")
    print("Elige una opción:")
    print("1. Añadir factura")
    print("2. Pagar factura")
    print("3. Terminar")
    print("====================")
    opcion = int(input())
    if opcion == 1:
        print("Has elegido, añadir una factura:")
        codigo = input("Código: ")
        coste = int(input("Coste: "))
        cod.append(codigo)
        cost.append(coste)
        print("Se ha añadido una factura")
    elif opcion == 2:
        print("Has elegido, pagar una factura:")
        codigo = input("Código: ")
        if codigo in cod:
            posicion = cod.index(codigo)
            print("Se ha pagado la factura %s, que costaba %d" % (cod[posicion], cost[posicion]))
            cost.remove(cost[posicion])
            cod.remove(cod[posicion])
        else:
            print("La factura introducida no existe")
    elif opcion == 3:
        print("Terminando la gestión...")
    else:
        print("Esa opción no existe D:")

