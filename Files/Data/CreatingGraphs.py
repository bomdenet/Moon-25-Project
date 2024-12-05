import matplotlib.pyplot as mtp


def GraphTimeMassa():
    mtp.xlabel("Время, c")
    mtp.ylabel("Масса, кг")
    mtp.plot(time, massa)
    mtp.show()

def GraphTimeHeight():
    mtp.xlabel("Время, с")
    mtp.ylabel("Высота, м")
    mtp.plot(time, height)
    mtp.show()

def GraphTimeSpeed():
    mtp.xlabel("Время, с")
    mtp.ylabel("Скорость, м/c")
    mtp.plot(time, speed)
    mtp.show()

def GraphHeightSpeed():
    mtp.xlabel("Высота, м")
    mtp.ylabel("Скорость, м/c")
    mtp.plot(height, speed)
    mtp.show()

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

#GraphTimeMassa()
#GraphTimeHeight()
GraphTimeSpeed()
#GraphHeightSpeed()