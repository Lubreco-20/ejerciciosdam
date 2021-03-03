#Print the second item in the fruits list
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#Change the value from "apple" to "kiwi", in the fruits list
fruits[0] = "kiwi"

#Use the append method to add "orange" to the fruits list
fruits.append("orange")

#Use the insert method to add "lemon" as the second item in the fruits list
fruits.insert(2, "lemon")

#Use the remove method to remove "banana" from the fruits list
fruits.remove("banana")

#Use negative indexing to print the last item in the list
print(fruits[-1])

#Use a range of indexes to print the third, fourth, and fifth item in the list
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon")
print(fruits[2:5])

#Use the correct syntax to print the number of items in the list
print(len(fruits))

#Use the correct syntax to print the first item in the fruits tuple
print(fruits[0])

#heck if "apple" is present in the fruits set
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#Use the add method to add "orange" to the fruits set
fruits.add("orange")

#Use the correct method to add multiple items (more_fruits) to the fruits set
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#Use the discard method to remove "banana" from the fruits set
fruits.discard("banana")

#Ejercicio 2
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
print(asignaturas)

#Ejercicio 3
print("Yo estudio %s." % (asignaturas[0:5]))

#Ejercicio 4
print("Dime una asignatura, a ver si existe en nuestra lista")
pregunta = input()
if pregunta in asignaturas:
  print("Existe en nuestra lista")
else:
  print("No existe en nuestra lista")

#Ejercicio 5
numeros = [1, 2, 3]
cadenas = ["hola", "mundo"]
print("Numeros antes: " + str(numeros))
print("Cadenas antes: " + str(cadenas))
numeros.append(4)
cadenas.append("cruel")
print("Numeros ahora: " + str(numeros))
print("Cadenas ahora: " + str(cadenas))

#Ejercicio 6
a = {"jake", "john", "eric"}
b = {"john", "jill"}
c = a.difference(b)
print("En el grupo b no estan " + str(c))

#Ejercicio 7
x = range(6)
for n in x:
  print(n**2)