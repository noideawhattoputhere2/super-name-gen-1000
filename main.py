print("welcome to name gen 1000")
input("enter to start")
yogenerated = ["",""]
import random
import time
repeat = round(random.random() * 10)+round(random.random() * 10)+round(random.random() * 10)
repeatrepeat = int(input("amount of generates"))
yogenerated.clear()
HOW = 0
part1 = 0
part2 = 0
part3 = 0
part4 = 0
part1 = input("part1")
part2 = input("part2")
part3 = input("part3")
part4 = input("part4")
part5 = input("part5")
part6 = input("part6")
part7 = input("part7")
part8 = input("part8")
part9 = input("part9")
part10 = input("part10")
part11 = input("part1")
part12 = input("part2")
part13 = input("part3")
part14 = input("part4")
part15 = input("part5")
part16 = input("part6")
part17 = input("part7")
part18 = input("part8")
part19 = input("part9")
part20 = input("part10")
part21 = input("part1")
part22 = input("part2")
part23 = input("part3")
part24 = input("part4")
part25 = input("part5")


while True:
    while repeatrepeat > 0:
        while repeat > 0:
            R = random.random()
            if 0.04 < R < 0:
                yogenerated.append(part1)
            if 0.08 < R < 0.04:
                yogenerated.append(part2)
            if 0.04 < R < 0.08:
                yogenerated.append(part3)
            if 0.08 <= R <= 0.12:
                yogenerated.append(part4)
            if 0.12 < R < 0.16:
                yogenerated.append(part5)
            if 0.16 < R < 0.20:
                yogenerated.append(part6)
            if 0.20 < R < 0.24:
                yogenerated.append(part7)
            if 0.24 < R < 0.28:
                yogenerated.append(part8)
            if 0.28 < R < 0.32:
                yogenerated.append(part9)
            if 0.32 < R < 0.36:
                yogenerated.append(part10)
            if 0.36 < R < 0.40:
                yogenerated.append(part11)
            if 0.40 < R < 0.44:
                yogenerated.append(part12)
            if 0.44 < R < 0.48:
                yogenerated.append(part13)
            if 0.48 < R < 0.52:
                yogenerated.append(part14)
            if 0.52 < R < 0.56:
                yogenerated.append(part15)
            if 0.56 < R < 0.60:
                yogenerated.append(part16)
            if 0.60 < R < 0.64:
                yogenerated.append(part17)
            if 0.64 < R < 0.68:
                yogenerated.append(part18)
            if 0.68 < R < 0.72:
                yogenerated.append(part19)
            if 0.72 < R < 0.76:
                yogenerated.append(part20)
            if 0.76 < R < 0.80:
                yogenerated.append(part21)
            if 0.80 < R < 0.84:
                yogenerated.append(part22)
            if 0.84 < R < 0.88:
                yogenerated.append(part23)
            if 0.88 < R < 0.92:
                yogenerated.append(part24)
            if 0.92 < R < 0.96:
                yogenerated.append(part25)
            repeat = repeat - 1
        repeatrepeat = repeatrepeat - 1
        test = random.random()
        print(yogenerated)
        print(repeatrepeat)
        repeat = round(random.random() * 10)
        yogenerated.clear()
    input("enter to restart")
    repeatrepeat = int(input("amount of repeats"))