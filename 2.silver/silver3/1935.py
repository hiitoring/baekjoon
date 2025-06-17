t = int(input()) # 피연산자의 개수
sik = list(input()) # 후위 표기식
nums = [] # A,B,C,D ... 의 값의 리스트
answer = [] 
for _ in range(t):
    num = int(input())
    nums.append(num) 
for i in sik:
    if i.isalpha() :
        answer.append(nums[ord(i) - ord("A")]) # ex) 피연산자"A" = nums[67-67] = A의 값 도출 
    else:
        b = answer.pop()
        a = answer.pop()
        if i == "+":
            answer.append(a+b)
        if i == "-":
            answer.append(a-b)
        if i == "*":
            answer.append(a*b)
        if i == "/":
            answer.append(a/b)
realanswer = answer[0]
print(f"{realanswer:.2f}") #f-string을 이용해 소숫점 2자리까지 출력
        