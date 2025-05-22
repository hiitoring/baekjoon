n = int(input())
vocaset = set()
for _ in range(n):
    voca = input()
    vocaset.add(voca)
vocali = list(vocaset)
vocali.sort(key = lambda x : (len(x), x))
for i in vocali:
    print(i)