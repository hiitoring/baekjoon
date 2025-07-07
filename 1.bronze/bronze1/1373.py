two = list(input())
answer = []
while two:
    eight = 0
    for i in range(3):
        if two:
            gop = 2 ** i
            if two.pop() == "1":
                eight += gop
    answer.append(eight)
while answer:
    print(answer.pop(),end="")

    