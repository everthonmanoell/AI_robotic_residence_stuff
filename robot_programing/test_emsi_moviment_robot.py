import time

import pigpio

# pi = pigpio.pi()

# pin = 19
# angle = 0

# pi.set_servo_pulsewidth(pin, 1500 + angle * 10) # conversão do ângulo em largura de pulso (1500 é o centro, 1000 é -50 graus, 2000 é +50 graus)
# time.sleep(1)

# pi.set_servo_pulsewidth(pin, 0)
# pi.stop()


#cacular a velocidade de cada ponto para chegar até o qj
q0 = 0
qj = 90
v_max = 30
a_max = 10

t_acc = v_max / a_max # tempo de aceleração
d_ac = 1/2 * a_max * pow(t_acc,2) # distância percorrida durante a aceleração
d_total = abs(qj - q0) # distância total a ser percorrida


# print("d_total:", d_total)
# print("d_dac:", d_ac)
# print("t_acc:", t_acc)


def trapezoid( qi, qf):
    V_max = 20 # velocidade máxima (m/s)
    A_max = 10 # aceleração máxima (m/s²)
    ts = 0.02 # sampling time (s) (50 Hz) (1/50 = 0.02 or 1/frequence)

    #time to accelerate and decelerate
    delta_time_acc = V_max / A_max

    # First part - acceleration
    nbSteps_acc = int(delta_time_acc / ts)
    time_vector = range(0, nbSteps_acc) # tempo de 0 até o número de passos de aceleração


    #distance during acceleration
    delta_distance_acc = 0.5 * A_max * pow(delta_time_acc, 2)

    #distance with constant speed
    delta_distance_cst = abs(qf - qi) - 2 * delta_distance_acc

    #time with constant speed
    delta_time = delta_distance_cst / V_max

    p = []

    for s in time_vector:
        t = s * ts
        v = A_max * t
        p.append(0.5 * A_max * pow(t, 2))  # posição durante a aceleração
        print("Acceleration phase - Time: {:.2f} s, Velocity: {:.2f} m/s".format(t, v))

    
    




print(trapezoid (0, 90))

    