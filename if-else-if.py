#Ejercicio1
#Print "Hello World" if a is greater than b.
a = 50
b = 10
if a > b:
    print("Hello world!")

#Imprime "Hola mundo" si ano es igual a b.
a = 50
b = 10
if a != b:
    print("Hola mundo")

#Print "Yes" if a is equal to b, otherwise print "No".
a = 50
b = 10
if a == b:
  print("Si")
else:
  print("No")

#Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".
a = 50
b = 10
if a == b:
  print("1")
elif a > b:
  print("2")
else:
  print("3")

#Print "Hello" if a is equal to b, and c is equal to d.
c = 7
d = 7
if a == b and c == d:
  print("Hello")

#Print "Hello" if a is equal to b, or if c is equal to d.
if a == b or c == d:
  print("Hello")

#This example misses indentations to be correct. Insert the missing indentation to make the code correct:
if 5 > 2:
  print("Five is greater than two!")

#Use the correct short hand syntax to write the following conditional expression in one line:
print("Yes") if 5 > 2 else print("No")

#Ejercicio 2
print("¿Cuantos años tienes?")
edad = input()
if int(edad) > 18:
    print("Eres mayor de edad")
else:
    print("Aún eres menor de edad")

#Ejercicio 3
contraseña = "contraseña"
print("Introduce una contraseña")
validar = input()
if contraseña == validar:
  print("La contraseña es válida")
else:
  print("La contraseña es inválidad")

#Ejercicio 4
print("Escribe un número")
numero = input()
if int(numero)%2 == 0:
  print("El número es primo")
else:
  print("El número es impar")

#Ejercicio 5
print("Introduce un dividendo")
numero1 = input()
dividendo = int(numero1)
print("Introduce un divisor")
numero2 = input()
divisor = int(numero2)
if divisor == 0:
  print("ERROR")
else:
  resultado = dividendo/divisor
  print("El resultado es %d" % (resultado))