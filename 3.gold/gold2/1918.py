sik = list(input())
result = []
imsi = []
sanza = {
    "+" : 1,
    "-" : 1,
    "*" : 2,
    "/" : 2
}
for i in sik:
    if i.isalpha():
        result.append(i)
    elif i == "(":
        imsi.append(i)
    elif i == ")":
        while imsi and imsi[-1] != "(":
            result.append(imsi.pop())
        imsi.pop()
    else:
        while imsi and imsi[-1] != "(" and sanza.get(imsi[-1],0) >= sanza[i]:
            result.append(imsi.pop())
        imsi.append(i)
while imsi:
    result.append(imsi.pop())
print("".join(result))