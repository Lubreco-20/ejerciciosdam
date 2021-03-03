#Ejercicio 1
#Define una clase “animal” con atributos color, número de 
#patas y especie (la especie se obtiene del nombre de la 
#propia clase, con self.__class__.__name__
class animal:
    def __init__(self,color,patas,especie):
        self.color = color
        self.patas = patas
        self.especie = especie

#Ejercicio 2
#Define el método necesario para imprimir la clase el 
#siguiente formato al llamar al método print: {especie} 
#con {patas} patas y de color {color}
    def __str__(self):
        return "Especie: " +str(self.especie) + ", patas: " + str(self.patas) + ", color: " + str(self.color) 

#Ejercicio 3
#Define la jerarquía de clases para los animales lobo, 
# que siempre tiene 4 patas, oveja, que siempre tiene 
# 4 patas y puede ser blanca o negra, serpiente y loro.
lobo = animal("Grises, blancos y negros", 4, "Canido")
oveja = animal("Blanca o negra", 4, "Ovino")
serpiente = animal("Muchos colores", 0, "Reptil")
loro = animal("Muchos colores", 2, "Ave")
#Ejercicio 4
#Define una clase Caja en la que meter a los animales a través 
# de un método que acepte vargars. Cada vez que se crea una 
# caja, se le asigna un id de forma incremental (0, 1, 2...). 
# Define el método para imprimir la caja con su id y contenido 
# (animales) a través del método print

#Ejercicio 5
#Define para “Caja” el método “animales_por_patas” que devuelva 
# la lista de los animales que tienen el número de patas especificado 
# y están en la caja (usa la compresión de listas)
