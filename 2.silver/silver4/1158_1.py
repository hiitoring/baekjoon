from collections import deque
n, k = map(int,input().split())
nums = deque()
answer = []
for i in range(n): # 덱에 숫자 추가
    nums.append(i+1)
for _ in range(n): 
    nums.rotate(-k+1) # 숫자를 k-1 만큼 역순으로 회전
    answer.append(nums.popleft()) #k번째 숫자를 pop
print("<"+", ".join(map(str,answer))+">")
