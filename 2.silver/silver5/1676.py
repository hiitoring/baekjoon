n = int(input())
fac = 1
count = 0
for i in range(1,n+1):
    fac = fac * i
fac = str(fac)
for j in reversed(fac):
    if j == "0":
        count += 1
    else:
        break
print(count)