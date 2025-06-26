n = int(input())
count = 0
for i in range(5,n+1,5):
    count += 1
    if i % 25 == 0:
        count += 1
    if i % 125 == 0:
        count += 1
print(count)