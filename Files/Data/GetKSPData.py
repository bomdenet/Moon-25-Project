import os
import krpc
import time
import numpy


os.system("cls")
print("Подключаюсь к кораблю")
conn = krpc.connect(name="Муна-25 1")
vessel = conn.space_center.active_vessel
earth = conn.space_center.bodies["Kerbin"]

ss = "время, масса, высота, скорость"
t = 0
while vessel.orbit.periapsis_altitude < 200000:
    ss += f"\n{t:.2f}, {vessel.mass:.2f}, {vessel.flight().mean_altitude:.2f}, {numpy.linalg.norm(vessel.velocity(earth.reference_frame)):.2f}"
    t += 0.02
    time.sleep(0.02)

f = open("Files/Data/KSP_Stats.txt", "w", encoding="UTF-8")
f.write(ss)
print("Файл сохранён")