t = int(input())
for _ in range(t):
    sen = []
    rsen = []
    sen = input().split()
    for i in sen:
        rsen.append(i[::-1]) #슬라이싱 len(rsen - 1) to 0 step = -1
    print(*rsen)