import time
import numpy

class Constats:
    def I(n, h):
        if n == 0:
            return Constats.I_0_first_stage - (Constats.I_0_first_stage - Constats.I_1_first_stage) * Constats.P_a(h) / Constats.P_0
        elif n == 1:
            return Constats.I_0_second_stage - (Constats.I_0_second_stage - Constats.I_1_second_stage) * Constats.P_a(h) / Constats.P_0
        elif n == 2:
            return Constats.I_0_third_stage - (Constats.I_0_third_stage - Constats.I_1_third_stage) * Constats.P_a(h) / Constats.P_0

    def U_e(n, h):
        return Constats.I(n, h) * Constats.g(h)

    def q(n, h):
        if n == 0:
            return Constats.q_first_stage * Constats.I_0_first_stage / Constats.I(n, h)
        elif n == 1:
            return Constats.q_second_stage * Constats.I_0_second_stage / Constats.I(n, h)
        elif n == 2:
            return Constats.q_third_stage * Constats.I_0_third_stage / Constats.I(n, h)

    def Find_P_e(n):
        if n == 0:
            a = Constats.P_0 * (Constats.q(n, 200000) * Constats.U_e(n, 200000) - Constats.F_0_first_stage)
            b = Constats.F_1_first_stage - Constats.q(n, 0) * Constats.U_e(n, 0) + Constats.q(n, 200000) * Constats.U_e(n, 200000) - Constats.F_0_first_stage
        elif n == 1:
            a = Constats.P_0 * (Constats.q(n, 200000) * Constats.U_e(n, 200000) - Constats.F_0_second_stage)
            b = Constats.F_1_second_stage - Constats.q(n, 0) * Constats.U_e(n, 0) + Constats.q(n, 200000) * Constats.U_e(n, 200000) - Constats.F_0_second_stage
        elif n == 2:
            a = Constats.P_0 * (Constats.q(n, 200000) * Constats.U_e(n, 200000) - Constats.F_0_third_stage)
            b = Constats.F_1_third_stage - Constats.q(n, 0) * Constats.U_e(n, 0) + Constats.q(n, 200000) * Constats.U_e(n, 200000) - Constats.F_0_third_stage
        return a / b
    
    def Find_S_e(n):
        if n == 0:
            a = Constats.F_1_first_stage - Constats.q(n, 0) * Constats.U_e(n, 0)
            b = Constats.P_e_first_stage - Constats.P_0
        elif n == 1:
            a = Constats.F_1_second_stage - Constats.q(n, 0) * Constats.U_e(n, 0)
            b = Constats.P_e_second_stage - Constats.P_0
        elif n == 2:
            a = Constats.F_1_third_stage - Constats.q(n, 0) * Constats.U_e(n, 0)
            b = Constats.P_e_third_stage - Constats.P_0
        return a / b

    def P_a(h):
        if h <= 100000:
            return Constats.P_0 * Constats.e**(-Constats.M * Constats.g(h) * h / Constats.R / Constats.T_Kelvin(h))
        else:
            return 0

    def T_Kelvin(h):
        if h <= 11000:
            return Constats.T_0 - 6.5 * h / 1000
        elif h <= 20000:
            return Constats.T_0 - 71.5
        elif h <= 50000:
            return Constats.T_0 - 71.5 + 54 * (h - 20000) / 30000
        elif h <= 80000:
            return Constats.T_0 - 17.5 - 72.1 * (h - 50000) / 30000
        elif h <= 100000:
            return Constats.T_0 - 89.6
        elif h <= 150000:
            return Constats.T_0 - 89.6 + 429 * (h - 100000) / 50000
        elif h <= 200000:
            return Constats.T_0 + 339.4 + 226.8 * (h - 150000) / 50000
        elif h <= 300000:
            return Constats.T_0 + 566.2 + 116 * (h - 200000) / 100000 
        elif h <= 500000:
            return Constats.T_0 + 682.2 + 29.6 * (h - 300000) / 200000
        return 1000

    def g(h):
        return Constats.G * Constats.massa_Earth / (Constats.radius_Earth + h) ** 2

    def Initialization():
        Constats.P_e_first_stage = Constats.Find_P_e(0)
        Constats.S_e_first_stage = Constats.Find_S_e(0)
        Constats.P_e_second_stage = Constats.Find_P_e(1)
        Constats.S_e_second_stage = Constats.Find_S_e(1)
        Constats.P_e_third_stage = Constats.Find_P_e(2)
        Constats.S_e_third_stage = Constats.Find_S_e(2)


    # Физические и математические константы
    time_scip = 0.01
    G = 6.67 * 10**(-11)
    P_0 = 101325
    M = 0.02898
    R = 8.314
    e = 2.718
    T_0 = 288.2

    # Параметры связанный с Землёй
    massa_Earth = 5.976 * 10**24
    radius_Earth = 6.378 * 10**6


    # Параметры связанные с ракетой
    dry_massa_first_stage = 6890
    massa_fuel_first_stage = 22800
    q_first_stage = 88.35 #409,8 88.35 0.215
    F_1_first_stage = 247000
    F_0_first_stage = 260000
    I_1_first_stage = 285
    I_0_first_stage = 300
    P_e_first_stage = 0 #Инициализаия позже
    S_e_first_stage = 0 #Инициализаия позже

    dry_massa_second_stage = 8038
    massa_fuel_second_stage = 33200
    q_second_stage = 172.13 #364 172.13 0.47
    F_1_second_stage = 568750
    F_0_second_stage = 650000
    I_1_second_stage = 280
    I_0_second_stage = 320
    P_e_second_stage = 0 #Инициализаия позже
    S_e_second_stage = 0 #Инициализаия позже

    dry_massa_third_stage = 2722
    massa_fuel_third_stage = 3993
    q_third_stage = 72.835 #123 72.835 0.59
    F_1_third_stage = 64286
    F_0_third_stage = 250000
    I_1_third_stage = 90
    I_0_third_stage = 350
    P_e_third_stage = 0 #Инициализаия позже
    S_e_third_stage = 0 #Инициализаия позже

    other_massa = 9200


class Ship:
    velocity = [0, 0, 0]
    steering = [0, 0, 0]
    height = 0
    throttle = 0
    stage = 0
    massa_fuel_first_stage = Constats.massa_fuel_first_stage
    massa_fuel_second_stage = Constats.massa_fuel_second_stage
    massa_fuel_third_stage = Constats.massa_fuel_third_stage

    def FixedUpdate():

        return

    def speed():
        return numpy.linalg.norm(Ship.velocity)

    def I():
        if Ship.stage == 0:
            return Constats.I_0_first_stage - (Constats.I_0_first_stage - Constats.I_1_first_stage) * Ship.P_a() / Constats.P_0
        elif Ship.stage == 1:
            return Constats.I_0_second_stage - (Constats.I_0_second_stage - Constats.I_1_second_stage) * Ship.P_a() / Constats.P_0
        elif Ship.stage == 2:
            return Constats.I_0_third_stage - (Constats.I_0_third_stage - Constats.I_1_third_stage) * Ship.P_a() / Constats.P_0

    def massa():
        if Ship.stage == 0:
            return Ship.massa_fuel_first_stage * 4 + Ship.massa_fuel_second_stage + Ship.massa_fuel_third_stage +\
                   Constats.dry_massa_first_stage * 4 + Constats.dry_massa_second_stage +\
                   Constats.dry_massa_third_stage + Constats.other_massa
        elif Ship.stage == 1:
            return Ship.massa_fuel_second_stage + Ship.massa_fuel_third_stage + Constats.dry_massa_second_stage +\
                   Constats.dry_massa_third_stage + Constats.other_massa
        elif Ship.stage == 2:
            return Ship.massa_fuel_third_stage + Constats.dry_massa_third_stage + Constats.other_massa
        else:
            return Constats.other_massa

    def U_e():
        return Ship.I() * Ship.g()

    def q():
        if Ship.stage == 0:
            return Constats.q_first_stage * Constats.I_0_first_stage / Ship.I()
        elif Ship.stage == 1:
            return Constats.q_second_stage * Constats.I_0_second_stage / Ship.I()
        elif Ship.stage == 2:
            return Constats.q_third_stage * Constats.I_0_third_stage / Ship.I()

    #???
    def F():
        if Ship.stage == 0:
            return Constats.F_0_first_stage - (Constats.F_0_first_stage - Constats.F_1_first_stage) * Ship.P_a() / Constats.P_0
        elif Ship.stage == 1:
            return Constats.F_0_second_stage - (Constats.F_0_second_stage - Constats.F_1_second_stage) * Ship.P_a() / Constats.P_0
        elif Ship.stage == 2:
            return Constats.F_0_third_stage - (Constats.F_0_third_stage - Constats.F_1_third_stage) * Ship.P_a() / Constats.P_0

    def g():
        return Constats.G * Constats.massa_Earth / (Constats.radius_Earth + Ship.height) ** 2
    
    def P_a():
        if Ship.height <= 100000:
            return Constats.P_0 * Constats.e**(-Constats.M * Ship.g() * Ship.height / Constats.R / Ship.T_Kelvin())
        else:
            return 0
    
    def T_Kelvin():
        if Ship.height <= 11000:
            return Constats.T_0 - 6.5 * Ship.height / 1000
        elif Ship.height <= 20000:
            return Constats.T_0 - 71.5
        elif Ship.height <= 50000:
            return Constats.T_0 - 71.5 + 54 * (Ship.height - 20000) / 30000
        elif Ship.height <= 80000:
            return Constats.T_0 - 17.5 - 72.1 * (Ship.height - 50000) / 30000
        elif Ship.height <= 100000:
            return Constats.T_0 - 89.6
        elif Ship.height <= 150000:
            return Constats.T_0 - 89.6 + 429 * (Ship.height - 100000) / 50000
        elif Ship.height <= 200000:
            return Constats.T_0 + 339.4 + 226.8 * (Ship.height - 150000) / 50000
        elif Ship.height <= 300000:
            return Constats.T_0 + 566.2 + 116 * (Ship.height - 200000) / 100000 
        elif Ship.height <= 500000:
            return Constats.T_0 + 682.2 + 29.6 * (Ship.height - 300000) / 200000
        return 1000


Constats.Initialization()

Ship.height = 200000
print(Ship.F())

'''for i in range(1, 60):
    Ship.height = 0
    a0 = (Constats.F_1_first_stage - Ship.q() * Ship.U_e())
    a = (Constats.F_1_first_stage - Ship.q() * Ship.U_e()) / i * 20 + Ship.P_a()
    Ship.height = 200000
    b0 = (Constats.F_0_first_stage - Ship.q() * Ship.U_e())
    b = (Constats.F_0_first_stage - Ship.q() * Ship.U_e()) / i * 20 + Ship.P_a()
    print(f"{i / 20:.2f}, {a:.2f}, {b:.2f}, {a0:.2f}, {b0:.2f}")'''

'''t = 0
ss = "время, масса, высота, скорость"
while Ship.periapsis < 200000:
    ss += f"\n{t:.2f}, {Ship.massa:.2f}, {Ship.height:.2f}, {Ship.speed:.2f}"
    t += time_scip
    time.sleep(time_scip)

f = open("Files/Data/MathModel_Stats.txt", "w", encoding="UTF-8")
f.write(ss)
print("Файл сохранён")'''