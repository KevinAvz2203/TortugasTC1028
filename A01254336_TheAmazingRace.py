# Kevin Valdez A01254336
# Domingo Laso A01252429
# 08 de septiembre del 2021
# TC1028 G3

# The Amazing Race proyecto medio termino 

""" Requisitos: 
* n tortuguitas donde n al menos es 1)                                                                                                                      listo
* Distinto color por cada tortuguita                                                                                                                        listo
* Pedir el nombre para cada una de las tortuguitas                                                                                                          listo
* Todas las tortuguitas deben avanzar en intervalos de distancias random [0..distancia] cada vez. El avance es distinto para cada tortuguita cada vez       listo
• Pedir al usuario la entrada de “ distancia                                                                                                                listo
• Deben correr en 2 formas opcionalmente                                                                                                                    listo
    1. Avanzan una distancia random cada Click de mouse o cada que insertan un INPUT value                                                                  listo
    2. Avanzan en forma libre ( considerando la distancia random) desde la marca de inicio hasta llegar a la Meta                                           listo
• El programa debe permitir iniciar otra vez con las tortuguitas en la marca de salida sin tener que reiniciar el programa                                  listo
• Cuando una tortuguita llega a la línea de Meta el programa debe detenerse pero no terminar ) y avisar QUIÉN es la tortuguita ganadora                     listo
• Debido a que puede haber multiples carreras , deberás llevar control del numero de veces que gana cada tortuguita                                         Listo
• Al final, cuando se decide terminar el programa se debe imprimir cuántas veces ha Ganado cada tortuguita                                                  Listo
 """

import turtle
import time
import random
import winsound

WIDTH, HEIGHT = 840, 650

veces_que_gana_tortuga1 = 0
veces_que_gana_tortuga2 = 0
veces_que_gana_tortuga3 = 0
veces_que_gana_tortuga4 = 0

t1_nombre = input("Ingresa el nombre de la primera tortuga: ")
t2_nombre = input("Ingresa el nombre de la segunda tortuga: ")
t3_nombre = input("Ingresa el nombre de la tercera tortuga: ")
t4_nombre = input("Ingresa el nombre de la cuarta tortuga: ")

while True:

    # Funcion para definir distancia maxima 
    def definir_distancia():
        distancia = int(input("Ingresa la distancia maxima para avanzar por tortuga (en enteros): "))
        return distancia

    # Funcion donde se inicia la carrera
    def iniciar_carrera():
        tortugas = crear_tortugas()

        fantasma = turtle.Turtle()
        fantasma.hideturtle()
        fantasma.pencolor("white")
        fantasma.write("En sus marcas", align="center", font=("Calibri", 32, "bold"))
        time.sleep(1)
        fantasma.clear()

        fantasma.pencolor("white")
        fantasma.write("Listos", align="center", font=("Calibri", 32, "bold"))
        time.sleep(1)
        fantasma.clear()

        fantasma.pencolor("white")
        fantasma.write("Fuera!!", align="center", font=("Calibri", 32, "bold"))
        time.sleep(1)
        fantasma.clear()

        fantasma.penup()
        fantasma.setpos(-300, 280)
        fantasma.pendown()
        fantasma.pencolor("white")
        fantasma.write("Meta: ", font=("Comic Sans MS", 18, "normal"))
        fantasma.pensize(10)
        fantasma.forward(600)

        winsound.PlaySound("fast.wav", flags=winsound.SND_ASYNC)

        while True:
            for tortuga1 in tortugas:
                _distancia1 = random.randrange(1, distancia)
                tortuga1.forward(_distancia1)

                x1, y1 = tortuga1.pos()
                if y1 >= 290:
                    return tortugas.index(tortuga1)
    
            for tortuga2 in tortugas:
                _distancia2 = random.randrange(1, distancia)
                tortuga2.forward(_distancia2)

                x2, y2 = tortuga2.pos()
                if y2 >= 290:
                    return tortugas.index(tortuga2)

            for tortuga3 in tortugas:
                _distancia3 = random.randrange(1, distancia)
                tortuga3.forward(_distancia3)

                x3, y3 = tortuga3.pos()
                if y3 >= 290:
                    return tortugas.index(tortuga3)

            for tortuga4 in tortugas:
                _distancia4 = random.randrange(1, distancia)
                tortuga4.forward(_distancia4)

                x4, y4 = tortuga4.pos()
                if y4 >= 290:
                    return tortugas.index(tortuga4)

    # Funcion para spawnear las tortugas
    def crear_tortugas():
        tortugas = []
        espacio_x = WIDTH // 3

        tortuga1 = turtle.Turtle()
        tortuga1.shape("turtle")
        tortuga1.color("gold")
        tortuga1.left(90)
        tortuga1.penup()
        tortuga1.setpos(-WIDTH // 2 + 0.8 * espacio_x, -HEIGHT // 2 + 20)
        tortuga1.pendown()
        tortugas.append(tortuga1)
        
        tortuga2 = turtle.Turtle()
        tortuga2.shape("turtle")
        tortuga2.color("navy")
        tortuga2.left(90)
        tortuga2.penup()
        tortuga2.setpos(-WIDTH // 2.45 + 1 * espacio_x, -HEIGHT // 2 + 20)
        tortuga2.pendown()
        tortugas.append(tortuga2)

        tortuga3 = turtle.Turtle()
        tortuga3.shape("turtle")
        tortuga3.color("green")
        tortuga3.left(90)
        tortuga3.penup()
        tortuga3.setpos(WIDTH // 2.45 - 1 * espacio_x, -HEIGHT // 2 + 20)
        tortuga3.pendown()
        tortugas.append(tortuga3)
        
        tortuga4 = turtle.Turtle()
        tortuga4.shape("turtle")
        tortuga4.color("red")
        tortuga4.left(90)
        tortuga4.penup()
        tortuga4.setpos(WIDTH // 2 - 0.8 * espacio_x, -HEIGHT // 2 + 20)
        tortuga4.pendown()
        tortugas.append(tortuga4)

        return tortugas

    # Funcion para modificar la ventana de la app
    def pantalla_turtle():
        pantalla = turtle.Screen()
        pantalla.clearscreen()
        pantalla.setup(WIDTH, HEIGHT)
        pantalla.title("Tortugas a correr!!")
        pantalla.bgpic("background.gif")

    # Ejecuta el codigo de arriba hacia abajo
    distancia = definir_distancia()

    print("Los nombres de las tortugas son {0}, {1}, {2} y {3}".format(t1_nombre, t2_nombre, t3_nombre, t4_nombre))
    print("La distancia maxima a avanzar es: ", distancia)

    pantalla_turtle()
    ganador = iniciar_carrera()

    fantasma2 = turtle.Turtle()
    fantasma2.hideturtle()
    fantasma2.penup()
    fantasma2.setpos(0, 0)
    fantasma2.pendown()
    fantasma2.pencolor("white")

    winsound.PlaySound(None, winsound.SND_PURGE)

    if ganador == 0:
        print("El ganador es: ", t1_nombre)
        fantasma2.write("El ganador es: {0}".format(t1_nombre), align="center", font=("Calibri", 32, "bold"))
        veces_que_gana_tortuga1 += 1
    elif ganador == 1:
        print("El ganador es:", t2_nombre)
        fantasma2.write("El ganador es: {0}".format(t2_nombre), align="center", font=("Calibri", 32, "bold"))
        veces_que_gana_tortuga2 += 1
    elif ganador == 2:
        print("El ganador es:", t3_nombre)
        fantasma2.write("El ganador es: {0}".format(t3_nombre), align="center", font=("Calibri", 32, "bold"))
        veces_que_gana_tortuga3 += 1
    else:
        print("El ganador es:", t4_nombre)
        fantasma2.write("El ganador es: {0}".format(t4_nombre), align="center", font=("Calibri", 32, "bold"))
        veces_que_gana_tortuga4 += 1

    time.sleep(5)

    while True:
        respuesta = input("Run again? (y/n): ")
        if respuesta in ("y", "n"):
            break
        print("Input invalido")
    
    if respuesta == "y":
        continue
    else:
        print("La tortuga {0} ganó {1} veces y la tortuga {2} ganó {3} veces".format(t1_nombre, veces_que_gana_tortuga1, t2_nombre, veces_que_gana_tortuga2))
        print("La tortuga {0} ganó {1} veces y la tortuga {2} ganó {3} veces".format(t3_nombre, veces_que_gana_tortuga3, t4_nombre, veces_que_gana_tortuga4))

        print("Hasta la proxima")
        break