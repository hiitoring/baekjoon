num = [0] * 10
A = int(input())
B = int(input())
C = int(input())
result = A*B*C
str_result = str(result)

for i in str_result:
    num[int(i)] += 1

for n in range(10):
    print(num[n])