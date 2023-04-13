from rodi import RoDI
import time

robot = RoDI()

def reubicar():
    robot.move_stop()
    robot.pixel(20,0,0)
    robot.move_backward()
    time.sleep(0.1)
    robot.move_left()
    time.sleep(0.5)
    robot.move_forward()
    time.sleep(0.5)

def ataque():
    robot.move(100,100)


while True:
    try:
        distancia = robot.see()
        linea = robot.sense()
        robot.pixel(20,20,20)
        robot.move(30,30)
        time.sleep(0.1)
        inicio_de_ataque = None

        print("Distancia: " + str(distancia))
        print("Linea 1: " + str(linea[0]))
        print("Linea 2: " + str(linea[1]))

        if (linea[0] >= 100 or linea[1] >= 100):
            reubicar()
        if distancia < 15:
            ataque()
            inicio_de_ataque = time.time()
        if time.time() - inicio_de_ataque > 2:
            reubicar()


    except KeyboardInterrupt:
        robot.move_stop()
        break
