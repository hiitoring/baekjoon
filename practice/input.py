for _ in range(int(input())):
    gwal = input()
    count=0
    for i in range(len(gwal)):
        if gwal[i:i+1] == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            break
    if count == 0:
        print("YES")   
    else:
        print("NO")     