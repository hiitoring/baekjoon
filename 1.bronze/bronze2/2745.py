n , b = input().split()
b = int(b)
j = 0
result = 0
for i in n[::-1]:
    if i.isalpha():
        result += (ord(i) - 55) * (b ** j)
    else:
        result += int(i) * (b ** j)
    j += 1
print(result)