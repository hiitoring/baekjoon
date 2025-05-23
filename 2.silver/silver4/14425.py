#set을 이용한 in 사용 버전전
n, m = map(int,input().split())
nlist = set(sorted(input()for _ in range(n)))
mlist = list(sorted(input()for _ in range(m)))
count = 0
for i in mlist:
   if i in nlist:
      count += 1
print(count)