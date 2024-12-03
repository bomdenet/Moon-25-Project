import time
import numpy

class Constats:
    massa_first_stage = 0
    massa_fuel_first_stage = 0
    speed_eating_fuel_first_stage = 1590
    massa_second_stage = 0
    massa_third_stage = 0
    g = 9,807

class Ship:
    massa = 0
    height = 0
    speed = 0
    apoapsis = 0
    periapsis = 0

t = 0
ss = "время, масса, высота, скорость"
while Ship.periapsis < 200000:
    ss += f"\n{t:.2f}, {Ship.massa:.2f}, {Ship.height:.2f}, {Ship.speed:.2f}"
    t += 0.02
    time.sleep(0.02)

f = open("Files/Data/MathModel_Stats.txt", "w", encoding="UTF-8")
f.write(ss)
print("Файл сохранён")