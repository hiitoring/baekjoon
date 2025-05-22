n, m = map(int,input().split()) # n = 포켓몬의 개수, m = 문제의 개수
poketmon = {}
for i in range(n):
    poke = input()
    poketmon[poke] = str(i+1) # 키에 포켓몬 이름, 번호를 같이 저장
    poketmon[str(i+1)] = poke
for l in range(m):
    ques = input()
    if ques in poketmon: # 입력이 이름이라면 번호, 번호라면 이름 출력
        print(poketmon[ques])  
    else:
        print(poketmon[ques])
