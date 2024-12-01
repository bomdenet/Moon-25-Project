import os
import krpc
import time
import numpy


# Дополнительный функции
def FindAngle(v1, v2):
    return numpy.rad2deg(numpy.arccos((v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]) / (numpy.linalg.norm(v1) * numpy.linalg.norm(v2))))

def FindVectorVelocity():
    past_Vector_velocity = vessel.position(earth.reference_frame)
    time.sleep(0.1)
    new_Vector_velocity = vessel.position(earth.reference_frame)
    return ((new_Vector_velocity[0] - past_Vector_velocity[0]) * 10,
            (new_Vector_velocity[1] - past_Vector_velocity[1]) * 10,
            (new_Vector_velocity[2] - past_Vector_velocity[2]) * 10)

def CheckCanGoToMoon():
    Vector_Kerbin_Mun = moon.position(earth.reference_frame)
    Vector_ship_Mun = moon.position(vessel.reference_frame)
    Vector_velocity = FindVectorVelocity()
    
    if FindAngle(Vector_velocity, Vector_ship_Mun) > 90:
        angle_ship_Moon = -angle_ship_Moon

    a1 = (numpy.linalg.norm(Vector_Kerbin_Mun) + vessel.flight().mean_altitude + earth.equatorial_radius) / 2
    a2 = numpy.linalg.norm(Vector_Kerbin_Mun)
    angle_true = 180 * (1 - (a1/a2) ** 1.5)

    os.system("cls")
    print(f"Текущий угол: {angle_ship_Moon:.2f}°")
    print(f"Необходимый угол: {angle_true:.2f}°")
    return abs(angle_ship_Moon - angle_true) > 3.

def FindX():
    os.system("cls")

    b1 = vessel.mass / vessel.max_thrust
    b2 = (numpy.linalg.norm(vessel.velocity(moon.reference_frame)) ** 2) / (2 * vessel.flight().mean_altitude)
    g = (6.67 * (10 ** (-11))) * ((7.35 * (10 ** 22)) / ((moon.equatorial_radius + vessel.flight().mean_altitude) ** 2))

    true_force = b1 * (b2 + g)
    work_force = true_force
    if true_force > 0.5:
        work_force = 0.5 + (true_force - 0.5) * 3
    if work_force > 1:
        work_force = 1
    t = numpy.linalg.norm(vessel.velocity(moon.reference_frame)) / (vessel.max_thrust * true_force / vessel.mass - g)
    print(f"Скорость: {numpy.linalg.norm(vessel.velocity(moon.reference_frame)):.2f} м/с")
    print(f"Высота: {vessel.flight().mean_altitude:.2f} м")
    print(f"Масса корабля: {vessel.mass:.2f} кг")
    print(f"Воздействие гравитации: {g:.2f} м/с²")
    print(f"Необходимая работа двигателей: {true_force * 100:.2f}%")
    print(f"Работа двигателей: {work_force * 100:.2f}%")
    print(f"Ориентировочно посадка через: {t:.1f} с")

    return work_force


# Функции полёта
def WaitBeforeStart():
    os.system("cls")

    for i in range(3):
        print(3 - i)
        time.sleep(1)
        os.system("cls")
    
    print("ПОЕХАЛИ!")
    time.sleep(1)

def FirstStage():
    os.system("cls")

    print("Набираем высоту")
    vessel.auto_pilot.engage()
    vessel.auto_pilot.target_pitch_and_heading(90, 90)
    vessel.control.throttle = 1
    vessel.control.activate_next_stage()

    while vessel.flight().mean_altitude < 30000:
        vessel.auto_pilot.target_pitch_and_heading(90 - 50 * (vessel.flight().mean_altitude / 30000), 90)
        os.system("cls")
        stage_resources = vessel.resources_in_decouple_stage(
            stage=vessel.control.current_stage - 1,
            cumulative=False)
        print(f"Топливо LiquidFuel: {stage_resources.amount('LiquidFuel'):.2f}")
        print(f"Топливо Oxidizer: {stage_resources.amount('Oxidizer'):.2f}")
        print(f"Топливо SolidFuel: {stage_resources.amount('SolidFuel'):.2f}")
        time.sleep(0.1)
    
    vessel.auto_pilot.target_pitch_and_heading(20, 90)
    vessel.control.throttle = 0
    time.sleep(2)
    vessel.control.activate_next_stage()
    time.sleep(5)

def SecondStage():
    os.system("cls")

    print("Произвожу запуск второй ступени")
    vessel.control.throttle = 1
    while vessel.flight().mean_altitude < 80000:
        time.sleep(0.1)

    print("Вышли за пределы орбиты Земли. Произвожу сброс обтекателей")
    vessel.control.activate_next_stage()
    while vessel.orbit.apoapsis_altitude < 202500:
        time.sleep(0.1)

def CircleOrbit():
    os.system("cls")

    vessel.control.throttle = 0
    vessel.auto_pilot.target_pitch_and_heading(0, 90)
    while vessel.orbit.time_to_apoapsis > 12:
        os.system("cls")
        print("Выходим на апоцентр в 200км")
        print(f"До апоцентра осталось {vessel.orbit.time_to_apoapsis:.1f} секунд")
        time.sleep(0.1)
    vessel.control.throttle = 1

    while vessel.orbit.periapsis_altitude < 200000:
        os.system("cls")
        print(f"Апоцентр: {vessel.orbit.apoapsis_altitude:.2f} м")
        print(f"Перицентр: {vessel.orbit.periapsis_altitude:.2f} м")
        time.sleep(0.1)
    vessel.control.throttle = 0
    time.sleep(3)
    vessel.control.activate_next_stage()
    time.sleep(3)

def GoToMoon():
    os.system("cls")

    print("Подлетаем к точке отлёта")
    while CheckCanGoToMoon():
        time.sleep(0.1)
    
    print("Начинаем полёт к Луне")
    vessel.auto_pilot.reference_frame = vessel.orbital_reference_frame
    vessel.auto_pilot.target_direction = vessel.flight(vessel.orbital_reference_frame).prograde
    time.sleep(3)

    while vessel.orbit.apoapsis_altitude < moon.orbit.semi_major_axis:
        vessel.control.throttle = 1 - 0.9 * vessel.orbit.apoapsis_altitude / moon.orbit.semi_major_axis
        time.sleep(0.1)
    
    vessel.control.throttle = 0

def OnTheMoon():
    os.system("cls")

    print("Летим к Луне")
    while vessel.orbit.body != moon:
        time.sleep(0.1)
    vessel.control.activate_next_stage()
    
    if vessel.orbit.periapsis_altitude > 1000:
        print("Сбились с курса, начинаю выравнивание")

        past_Vector_velocity = vessel.position(earth.reference_frame)
        time.sleep(0.1)
        new_Vector_velocity = vessel.position(earth.reference_frame)
        if new_Vector_velocity[0] - past_Vector_velocity[0] > 0:
            if new_Vector_velocity[2] - past_Vector_velocity[2] > 0:
                vessel.auto_pilot.target_pitch_and_heading(0, 90)
            else:
                vessel.auto_pilot.target_pitch_and_heading(0, 270)
        else:
            if new_Vector_velocity[2] - past_Vector_velocity[2] > 0:
                vessel.auto_pilot.target_pitch_and_heading(0, 270)
            else:
                vessel.auto_pilot.target_pitch_and_heading(0, 90)
        
        time.sleep(5)
        while vessel.orbit.periapsis_altitude > 1000:
            vessel.control.throttle = 1
            print(f"Перицентр: {vessel.orbit.periapsis_altitude:.2f} м")
            time.sleep(0.1)
            os.system("cls")
        time.sleep(5)

        vessel.control.throttle = 0
        print("Направление выравнено, готовлюсь к посадке")

    while vessel.flight().mean_altitude < 100000:
        time.sleep(0.1)
    print("Начинаем посадку")
    
    vessel.auto_pilot.reference_frame = vessel.orbital_reference_frame
    vessel.auto_pilot.target_direction = vessel.flight(vessel.orbital_reference_frame).retrograde
    time.sleep(5)

    while vessel.flight().mean_altitude < 25000:
        vessel.control.throttle = 1 * FindX()
        time.sleep(0.1)
    
    vessel.control.throttle = 0
    time.sleep(1)
    vessel.control.activate_next_stage()
    time.sleep(1)
    for leg in vessel.parts.legs:
        leg.deployed = True
    
    while FindVectorVelocity() != 0:
        vessel.control.throttle = 1 * FindX()
        time.sleep(0.1)

    print("Посадка совершена, миссия успешна!")

def Fly():
    WaitBeforeStart()
    FirstStage()
    SecondStage()
    CircleOrbit()
    GoToMoon()
    OnTheMoon()

os.system("cls")
print("Подключаюсь к кораблю")
conn = krpc.connect(name="Муна-25 1")
vessel = conn.space_center.active_vessel
moon = conn.space_center.bodies["Mun"]
earth = conn.space_center.bodies["Kerbin"]
sun = conn.space_center.bodies["Sun"]

Fly()