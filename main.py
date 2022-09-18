import random
import time

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

puntaje = 0

iniciar_trivia = True
intentos = 0

print(RED + "Bienvenido a mi trivia sobre Star Wars" + RESET)

print("Probaremos tu conocimiento sobre el universo de Star Wars,suerte y que la fuerza te acompañe")

nombre = input(CYAN + "Ingresa tu nombre: " + RESET)

print("\n Hola" + YELLOW,nombre ,RESET +"responde las siguientes preguntas escribiendo y presionando 'Enter' para enviar tu respuesta\n")

print("Tienes"+ YELLOW, puntaje, RESET + "puntos \n")

#for numero_carga in range(5,0,-1):
  #print(numero_carga)
  #time.sleep(1)

while iniciar_trivia == True:
  intentos += 1
  puntaje = 0

  print( "\nIntento número: ", intentos)
  input("Presiona Enter para continuar")

  print(GREEN + "1) ¿De qué color era el sable de luz del maestro mace windu?" + RESET)
  print("a) rojo")
  print("b) morado")
  print("c) amarillo")
  print("d) azul")

  respuesta_1 = input(BLUE + "\n Tu respuesta: "+ RESET)

  while respuesta_1 not in ("a","b", "c","d", "x"):
    respuesta_1 = input("Debes responder a, b, c o d. Vuelve a ingresar tu respuesta: ")
  
  if respuesta_1 == "a":
    puntaje -= 5
    print("Respuesta Incorrecta")
  elif respuesta_1 == "c":
    puntaje += 5
    print("...")
  elif respuesta_1 == "d":
    puntaje / 2
    print("Estuviste cerca")
  elif respuesta_1 == "x":
    puntaje += 66
    print("Respuesta secreta obtuviste un puntaje extra")
  else:
    puntaje +=10  * 2
    print(GREEN + "Correcto" , MAGENTA + "morado"+ RESET, "es el color del sable de luz del maestro Mace Windu ")
  
  print("\n Gracias" + YELLOW, nombre, RESET + "por participar, tienes" + BLUE, puntaje, RESET +"puntos\n")

  time.sleep(3)
  print("Loading...")
  time.sleep(1)

  print(GREEN + "2) ¿Qué nombre tenía el wookie amigo de Han Solo?" + RESET)
  print("a) Qui Gon Jin ")
  print("b) Palpatine")
  print("c) Chewbacca")
  print("d) C-3PO")

  respuesta_2 = input(BLUE + "\n Tu respuesta: " + RESET)

  while respuesta_2 not in ("a","b", "c","d", "j"):
    respuesta_2 = input("Debes responder a, b, c o d. Vuelve a ingresar tu respuesta: ")
    
  if respuesta_2 == "a":
    puntaje -= 5
    print("...")
  elif respuesta_2 == "b":
    puntaje / 2
    print("Estuviste cerca")
  elif respuesta_2 == "d":
    puntaje -= 10
    print("Respuesta Incorrecta")
  elif respuesta_2 == "j":
    puntaje += 66
    print("Respuesta secreta obtuviste un puntaje extra")
  else:
    puntaje +=10  * 2
    print( GREEN + "Correcto" + RESET, MAGENTA +"Chewbacca" + RESET , "es el mejor amigo de Han Solo" )
  
  print("\n Gracias"+ YELLOW, nombre, RESET + "por participar, tienes" + BLUE, puntaje, RESET + "puntos\n")
  
  time.sleep(3)
  print("Loading...")
  time.sleep(1)
  
  print( GREEN + "3) ¿Cuál es el personaje con el mayor número de midiclorianos en Star Wars?" + RESET)
  print("a) Yoda")
  print("b) Anakin Skywalker")
  print("c) Conde Dooku")
  print("d) Obi Wan Kenobi")
  
  respuesta_3 = input(BLUE + "\n Tu respuesta: " + RESET)
  
  while respuesta_3 not in ("a","b", "c","d", "x"):
    respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_3 == "a":
    puntaje / 2
    print("Estuviste cerca")
  elif respuesta_3 == "c":
    puntaje += 5
    print("Respuesta incorrecta")
  elif respuesta_3 == "d":
    puntaje -= 5
    print("...")
  elif respuesta_3 == "x":
    puntaje += 66
    print("Respuesta secreta obtuviste un puntaje extra")
  else:
    puntaje +=10  * 2
    print(GREEN + "Correcto", RESET + "el personaje con mayor número de midiclorianos es ", MAGENTA + "Anakin Skywalker" + RESET)
  
  time.sleep(3)
  print("Loading...")
  time.sleep(1)

  print( GREEN + "4) ¿En qué estilo de combate con sable de luz se especializaba Obi Wan Kenobi?" + RESET)
  print("a) Forma IV:Ataru")
  print("b) Forma I:Shii-Cho")
  print("c) Forma VII:Vaapad")
  print("d) Forma III:Soresu")
  
  respuesta_4 = input(BLUE + "\n Tu respuesta: " + RESET)
  
  while respuesta_3 not in ("a","b", "c","d", "x"):
    respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_3 == "a":
    puntaje / 2
    print("Estuviste cerca")
  elif respuesta_3 == "c":
    puntaje += 5
    print("Respuesta incorrecta")
  elif respuesta_3 == "b":
    puntaje -= 5
    print("...")
  elif respuesta_3 == "x":
    puntaje += 66
    print("Respuesta secreta obtuviste un puntaje extra")
  else:
    puntaje +=10  * 2
    print(GREEN + "Correcto", RESET + "el estilo de combate en el que se especializaba Obi Wan Kenobi es la", MAGENTA + "Forma III:Soresu" + RESET)
  
  time.sleep(3)
  print("Loading...")
  time.sleep(1)
  
  
  
  print("\n Gracias"+ YELLOW, nombre, RESET + "por jugar mi trivia, se aprecia el intento")
    #time.sleep(1)

  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

  if repetir_trivia != "si":  # != significa "distinto"
   print("\nEspero", nombre, "te hayas divertido, hasta la próxima!")
   iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.