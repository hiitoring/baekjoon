import sys
sosu = [True] * 1000001 # 에라토스테네스의 체를 이용하여 소수 구하기
for i in range(2,int(len(sosu)**0.5)+1):
    for j in range(i*i,len(sosu),i):
        if sosu[j]:
            sosu[j] = False
while True: # n = a + b | a = 3...n , b = n - a
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
        for a in range(3,n//2+1,2):
            if sosu[a] and sosu[n-a]:
                print(f"{n} = {a} + {n-a}")
                break
        else:
            print("Goldbach's conjecture is wrong.")

