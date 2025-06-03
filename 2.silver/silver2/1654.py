 # 입력
n,k = map(int,input().split())
lines = [int(input()) for _ in range(n)]
start= 1         # 이진 탐색을 위한 start, end 설정
end = max(lines)
answer = 0
# check 함수 설정 (만든 랜선이 K이상이면 True 반환)
def check(mid):
  count = 0
  for i in lines:   
    count += i // mid # mid의 길이로 만들 수 있는 랜선의 수 누적합 
  return count >= k # 랜선의 수가 필요한 랜선의 수를 넘는다면 True 출력
# 이진탐색 (check = True or else)
while start <= end: # 이진 탐색의 기본(start가 end를 초과하면 종료)
  mid = (start + end) // 2 
  if check(mid):
    answer = mid # 필요 랜선의 수를 넘었다면 일단 mid를 answer에 입력 
    start = mid + 1 
  else:
    end = mid -1
print(answer)