import os
import krpc
import time
import numpy


os.system("cls")
print("Подключаюсь к кораблю")
conn = krpc.connect(name="Муна-25 1")
vessel = conn.space_center.active_vessel
moon = conn.space_center.bodies["Mun"]
earth = conn.space_center.bodies["Kerbin"]
sun = conn.space_center.bodies["Sun"]

ss = "время, масса, высота, скорость"
t = 0
while vessel.orbit.periapsis_altitude < 200000:
    ss += f"{str(t)}, {vessel.mass * 1000}, {vessel.flight().mean_altitude}, {numpy.linalg.norm(vessel.velocity(earth.reference_frame))}\n"
    t += 0.02
    time.sleep(0.02)

f = open("stats.txt", "w")
f.write(ss)