# 2,5의 쌍 한 개당 뒷자리 0은 + 1
# 그렇기때문에 2와 5중 적은 개수 = 0의 개수

# 2와 5의 개수를 찾아주는 함수
def count(x,y): 
    count = 0 
    # x를 y로 소인수분해하여 y의 개수 탐색
    while x >= y:    
        x //= y
        count += x
    return count

x, y = map(int,input().split())

# 조합에서의 5의 개수
cnt5 = count(x,5) - count(y,5) - count(x-y,5)
# 조합에서의 2의 개수
cnt2 = count(x,2) - count(y,2) - count(x-y,2)
# 2와 5중 작은 개수 출력
print(min(cnt5,cnt2))