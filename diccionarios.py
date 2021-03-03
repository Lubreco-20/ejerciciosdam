#Ejercicio 1.1
#Use the get method to print the value of the "model" key of the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(
car.get("model")
)

#Ejercicio 1.2
#Change the "year" value from 1964 to 2020.
car["year"] = 2020

#Ejercicio 1.3
#Add the key/value pair "color" : "red" to the car dictionary.
car["color"] = "red"

#Ejercicio 1.4
#Use the pop method to remove "model" from the car dictionary.
car.pop("model")

#Ejercicio 1.5
#Use the clear method to empty the car dictionary.
car.clear()

#Ejercicio 2
dinero = {
  "Euro": "€",
  "Dollar": "$",
  "Yen": "¥"
}
print("¿Qué divisa quieres?")
divisa = input()
if divisa == "Euro":
  print(dinero.get("Euro"))
elif divisa == "Dollar":
  print(dinero.get("Dollar"))
elif divisa == "Yen":
  print(dinero.get("Yen"))
else:
  print("No tenemos esa divisa")

#Ejercicio 3
personal = {}

print("¿Cómo te llamas?")
nombre = input()
print("¿Cuántos años tienes?")
años = input()
print("¿Dónde vives?")
direccion = input()
print("¿Cuál es tu número de teléfono?")
telefono = input()

personal["nombre"] = nombre
personal["años"] = años
personal["direccion"] = direccion
personal["telefono"] = telefono

print(personal.get("nombre") + " tiene " + personal.get("años") + " años, vive en " + personal.get("direccion") + " y su número de teléfono es " + personal.get("telefono"))

#Ejercicio 4
precios = {
  "manzana": 1.59,
  "melocoton": 1.99,
  "naranja": 2.29
}

print("¿Qué fruta quieres?")
fruta = input()
print("¿Cuántos kilos de fruta quieres?")
kilos = input()

if fruta == "manzana":
  frutaKilo = precios.get(fruta) * kilos
  print(kilos + " de manzanas cuestan: " + frutaKilo)
elif fruta == "melocoton":
  frutaKilo = precios.get(fruta) * kilos
  print(kilos + " de melocotones cuestan: " + frutaKilo)
elif fruta == "naranja":
  frutaKilo = precios.get(fruta) * kilos
  print(kilos + " de naranjas cuestan: " + frutaKilo)
else:
  print("No tenemos esa fruta en nuestro inventario")