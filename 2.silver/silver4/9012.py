n = int(input())
for _ in range(n):
    gwal = list(map(str,input()))
    count = 0
    for _ in range(len(gwal)):
        if gwal.pop() ==  ")":
            count += 1
        else:
          count -= 1
          if count < 0:
             break
    if count == 0 :
        print("YES")
    else:
        print("NO")