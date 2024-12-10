import matplotlib.pyplot as mtp


def GraphTimeMassa():
    mtp.xlabel("Время, c")
    mtp.ylabel("Масса, кг")
    mtp.plot(time_ksp, massa_ksp, label='KSP', color=ksp_color)
    mtp.plot(time_mm, massa_mm, label='Math model', color=mm_color)

def GraphTimeHeight():
    mtp.xlabel("Время, с")
    mtp.ylabel("Высота, м")
    mtp.plot(time_ksp, height_ksp, label='KSP', color=ksp_color)
    mtp.plot(time_mm, height_mm, label='Math model', color=mm_color)

def GraphTimeSpeed():
    mtp.xlabel("Время, с")
    mtp.ylabel("Скорость, м/c")
    mtp.plot(time_ksp, speed_ksp, label='KSP', color=ksp_color)
    mtp.plot(time_mm, speed_mm, label='Math model', color=mm_color)

def GraphHeightSpeed():
    mtp.xlabel("Высота, м")
    mtp.ylabel("Скорость, м/c")
    mtp.plot(height_ksp, speed_ksp, label='KSP', color=ksp_color)
    mtp.plot(height_mm, speed_mm, label='Math model', color=mm_color)

time_ksp = []
massa_ksp = []
height_ksp = []
speed_ksp = []
with open("Files/Data/KSP_Stats.txt", "r") as f:
    ss = f.read().split("\n")[1::]
    for i in range(len(ss)):
        ss[i] = ss[i].split(", ")
        time_ksp.append(float(ss[i][0]))
        massa_ksp.append(float(ss[i][1]))
        height_ksp.append(float(ss[i][2]))
        speed_ksp.append(float(ss[i][3]))

time_mm = []
massa_mm = []
height_mm = []
speed_mm = []
with open("Files/Data/MathModel_Stats.txt", "r") as f:
    ss = f.read().split("\n")[1::]
    for i in range(len(ss)):
        ss[i] = ss[i].split(", ")
        time_mm.append(float(ss[i][0]))
        massa_mm.append(float(ss[i][1]))
        height_mm.append(float(ss[i][2]))
        speed_mm.append(float(ss[i][3]))


ksp_color = "#008000"
mm_color = "#ff0000"
GraphTimeMassa()
mtp.legend()
mtp.show()
GraphTimeHeight()
mtp.legend()
mtp.show()
GraphTimeSpeed()
mtp.legend()
mtp.show()
GraphHeightSpeed()
mtp.legend()
mtp.show()

