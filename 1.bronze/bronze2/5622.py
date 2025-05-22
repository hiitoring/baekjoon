phone = input().lower()
time = 0
for i in phone:
    if i == "a" or i == "b"or i == "c":
        time += 3
    if i == "d" or i == "e"or i == "f":
        time += 4
    if i == "g" or i == "h"or i == "i":
        time += 5
    if i == "j" or i == "k"or i == "l":
        time += 6
    if i == "m" or i == "n"or i == "o":
        time += 7
    if i == "p" or i == "q"or i == "r" or i=="s":
        time += 8
    if i == "t" or i == "u"or i == "v":
        time += 9
    if i == "w" or i == "x"or i == "y" or i == "z":
        time += 10
print(time)