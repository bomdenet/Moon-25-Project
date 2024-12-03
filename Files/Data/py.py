time = []
massa = []
height = []
speed = []
with open("Files/Data/KSP_Stats.txt", "r") as f:
    ss = f.read().split("\n")[1::]
    for i in range(len(ss)):
        ss[i] = ss[i].split(", ")
        time.append(float(ss[i][0]))
        massa.append(float(ss[i][1]))
        height.append(float(ss[i][2]))
        speed.append(float(ss[i][3]))

ss = "время, масса, высота, скорость"
for i in range(len(time)):
    ss += f"\n{time[i]:.2f}, {massa[i] / 1000:.2f}, {height[i]:.2f}, {speed[i]:.2f}"

f = open("Files/Data/KSP_Stat.txt", "w")
f.write(ss)
print("Файл сохранён")