sent = list(input())
answer = []
for i in range(len(sent)):
    sent[i] = ord(sent[i])
for j in sent:
    if 65 <= j <= 77 or  97 <= j <= 109:
        answer.append(chr(j+13))
    elif 78 <= j <= 90 or 110 <= j <= 122 :
        answer.append(chr(j-13))
    else:
        answer.append(chr(j))
print("".join(answer))


