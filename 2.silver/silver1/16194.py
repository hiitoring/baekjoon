t = int(input())
card = [0] + list(map(int,input().split()))
value = [0] * (t+1)
value[1] = card[1]
for i in range(2,t+1):
    value[i] = card[i]
    for j in range(i-1,-1,-1):
        vigo = value[i-j] + card[j]
        if value[i] > vigo:
            value[i] = vigo
print(value[t])
