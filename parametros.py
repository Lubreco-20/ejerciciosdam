from sys import argv

script, user_name, script_name = argv
prompt = "> "

print("Hola %s, soy el script %s, pero me puedes llamar %s." % (user_name, script, script_name))
print("Me gustaría hacerte una pregunta")
print("Te gusto " + user_name + "?")
likes = input(prompt)
print("Vale %s, has dicho %s sobre mí" % (user_name, likes))
print("¿Que hobbies tienes?")
hobbies = input(prompt)
print("hmmm... Has dicho que te gusta %s... Interesante" % (hobbies))
print("¿Cuántos años tienes?")
edad = input(prompt)
print("Osea que tienes %s años, que es de tipo" % (edad))
print("Es de tipo: " + type(edad))
print("Estas son todas las respuestas que has dicho hasta ahora %s, %s y %s" % (likes, hobbies, edad))