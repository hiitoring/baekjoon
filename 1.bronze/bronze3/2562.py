num = []
for i in range(9):
    n = int(input())
    num.append(n)
count = num.index(max(num)) + 1
print(max(num))
print(count)