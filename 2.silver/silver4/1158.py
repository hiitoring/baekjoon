from collections import deque
n,k = map(int,input().split())
nums = deque() # 제거 할 숫자들이 모일 덱
imsi = deque() # 숫자들을 잠시 저장할 덱
answer = [] # 제거 된 숫자의 순열을 저장할 리스트트
for i in range(n): # 덱에 1 ~ n 까지의 정수 입력
    nums.append(i+1)
for _ in range(n): # 모든 숫자를 반복하여 제거
    i = 0
    while i < k: # k번만큼 숫자를 pop left 
        if len(nums) > 0: 
            imsi.append(nums.popleft())
            i += 1
        else: # 리스트를 순회했다면 제거되지 않은 숫자 투입
            for _ in range(len(imsi)):
                nums.append(imsi.popleft())
    answer.append(imsi.pop()) #k번째의 숫자를 제거
print("<",end="")
for i in range(len(answer)-1):
    print(answer[i],end=", ")
print(answer[-1],end="")
print(">")