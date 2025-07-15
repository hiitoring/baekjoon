n = int(input())
div = 2
while div ** 2 <= n:
    if n % div == 0:
        print(div)
        n //= div
    else:
        div += 1
if n > 1:
    print(n)