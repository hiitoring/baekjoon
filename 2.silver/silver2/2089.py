n = int(input())

if n == 0:
    print(0)
else:
    result = ''
    while n != 0:
        n, r = divmod(n, -2)
        if r < 0:
            n += 1
            r += 2
        result = str(r) + result
    print(result)