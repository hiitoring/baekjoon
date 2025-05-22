voca = input().upper()
countli = []
vocali = []
for i in set(voca):
    vocali += [i]
    count = voca.count(i)
    countli.append(count)
max_count = max(countli)
max_count_lo = countli.index(max_count)
if countli.count(max_count) > 1:
    print("?")
else :
    print(vocali[max_count_lo])