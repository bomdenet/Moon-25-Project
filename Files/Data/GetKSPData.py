import os
import krpc
import time
import numpy as np

# Очистка консоли и подключение
os.system("cls")
print("Подключаюсь к кораблю")
conn = krpc.connect(name="Муна-25 1")
vessel = conn.space_center.active_vessel
kerbin = conn.space_center.bodies['Kerbin']

# Заголовки для данных
ss = "время, масса, высота, скорость"
t = 0
while vessel.orbit.periapsis_altitude < 200000:
    flight = vessel.flight(kerbin.reference_frame)
    orbit = vessel.orbit
    absolute_velocity = np.linalg.norm(vessel.velocity(kerbin.reference_frame))
    orbital_velocity = np.linalg.norm(vessel.velocity(vessel.orbital_reference_frame))
    horizontal_speed = flight.horizontal_speed
    vertical_speed = flight.vertical_speed
    angular_velocity = np.linalg.norm(vessel.angular_velocity(vessel.reference_frame))
    true_air_speed = flight.true_air_speed
    pressure = flight.static_pressure
    temperature = flight.static_air_temperature
  


    # Форматирование строки с данными
    ss += f"\n{t}, {vessel.mass:.2f}, {flight.mean_altitude:.2f}, {absolute_velocity:.2f}"    
    t += 1
    time.sleep(1)

# Сохранение данных в файл
with open("Files/Data/KSP_Stats.txt", "w", encoding="UTF-8") as f:
    f.write(ss)
print("Файл сохранён")