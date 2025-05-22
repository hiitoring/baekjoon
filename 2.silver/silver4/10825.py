n = int(input())
score = []
for _ in range(n):
    name,kor,eng,math = input().split()
    oname = ord(name[0:1])
    score.append((name,int(kor),int(eng),int(math)))
score.sort(key=lambda x : (-x[1],x[2],-x[3],x[0]))

for i in range(n):
    manscore = score[i]
    print(manscore[0])