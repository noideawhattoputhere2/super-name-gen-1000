print("welcome to name gen 1000")
input("enter to start")
yogenerated = ["",""]
import random
import time
repeat = round(random.random() * 10)+round(random.random() * 10)+round(random.random() * 10)
repeatrepeat = 100000
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

while True:
    while repeatrepeat > 0:
        while repeat > 0:
            R = random.random()

            if R < 0.1 and R > 0:
                yogenerated.append(part1)
            if R < 0.2 and R > 0.1:
                yogenerated.append(part2)
            if R < 0.3 and R > 0.2:
                yogenerated.append(part3)
            if R < 0.4 and R > 0.3:
                yogenerated.append(part4)
            if R < 0.5 and R > 0.4:
                yogenerated.append(part5)
            if R < 0.6 and R > 0.5:
                yogenerated.append(part6)
            if R < 0.7 and R > 0.6:
                yogenerated.append(part7)
            if R < 0.8 and R > 0.7:
                yogenerated.append(part8)
            if R < 0.9 and R > 0.8:
                yogenerated.append(part9)
            if R < 1 and R > 0.9:
                yogenerated.append(part10)

            repeat = repeat - 1
        repeatrepeat = repeatrepeat - 1
        print(yogenerated)
        print(repeatrepeat)
        repeat = round(random.random() * 10)
        if yogenerated == ["t","e","n""e","i","g","e","r","0"]:
         HOW = HOW + 1
        yogenerated.clear()
    input("enter to restart")