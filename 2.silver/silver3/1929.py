import math
m,n = map(int,input().split())
sosu = [True] * (n+1) # True == 소수 기본 설정은 전부 소수
sosu[0] = False # 0과 1은 소수가 아님
sosu[1] = False
for i in range(2,int(math.sqrt(n)+1)): # 2부터 n의 제곱근까지 실행
    if sosu[i]: # i가 소수라면
        for j in range(i*i,n+1,i): 
        # i*i-1은 이미 실행 되었으므로 i*i부터 i의 배수를 False 처리
            sosu[j] = False
for i in range(m,n+1): 
    # index number와 1:1 대응 되므로 ex) i == 3 , sosu[i] == True 라면 3 출력 
    if sosu[i]:
        print(i)