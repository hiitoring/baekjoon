import sys
for i in sys.stdin:
    i= list(i.lstrip("\n"))
    answer = [0] * 4
    answer[3] = -1
    for j in i:
        if j.islower():
            answer[0] += 1
        elif j.isupper():
            answer[1] += 1
        elif j.isdigit():
            answer[2] += 1
        elif j.isspace():
            answer[3] += 1
    print(*answer)