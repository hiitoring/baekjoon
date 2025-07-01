# 최대공배수 산출 식
def GCD(x,y):
    while y:
        x,y = y, x%y
    return x

t = int(input())

for _ in range(t):
    nums = list(map(int,input().split()))
    count = 0
    # 마지막 숫자는 모든 쌍에 들어갔으니 제외
    for i in range(1,len(nums)-1):
        # 이미 누적한 숫자 쌍 제외
        for j in range(1+i,len(nums)):
            count += GCD(nums[i],nums[j])
    print(count)

                        
              
