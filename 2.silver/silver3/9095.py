t = int(input())
sumli = [0] * 12
sumli[1] = 1
sumli[2] = 2
sumli[3] = 4
for i in range(4,12):
        sumli[i] += sumli[i-1] + sumli[i-2] + sumli[i-3]
for _ in range(t):
    n = int(input())
    print(sumli[n])



