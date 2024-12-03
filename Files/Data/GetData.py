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
    ss += f"\n{str(t)}, {vessel.mass * 1000}, {vessel.flight().mean_altitude}, {numpy.linalg.norm(vessel.velocity(earth.reference_frame))}"
    t += 0.02
    time.sleep(0.02)

f = open("Files/Data/Stats.txt", "w")
f.write(ss)
print("Файл сохранён")