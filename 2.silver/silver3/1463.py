n = int(input())

dyn = [0] * (n+1)

for i in range(2,n+1):
    dyn[i] = dyn[i-1] + 1
    if i % 2 == 0:
        dyn[i] = min(dyn[i],dyn[i//2]+1)
    if i % 3 == 0:
        dyn[i] = min(dyn[i],dyn[i//3]+1)
print(dyn[n])