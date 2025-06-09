iron = list(input())
n = 0 # 쇠막대기의 개수
answer = 0 # 최종 쇠막대기의 개수수
while len(iron) > 0: # 괄호 리스트가 없어질 때까지 pop
        if iron.pop() == ")": 
            if iron[-1] == "(": # ()으로 생긴 배열이라면 레이저로 인식
                iron.pop() # "("도 함께 pop한 후에 
                answer += n # 나뉘어지기 때문에 쇠막대기 만큼 더하기
            else:
                n += 1 # 새로운 쇠막대기 추가
        else:       
            n -= 1 # 쇠막대기 제거
            answer += 1
print(answer)
