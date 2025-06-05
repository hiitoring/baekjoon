import sys #sys.stdin.readline 사용시는 .strip() 필수
def L(cursor): # 커서를 왼쪽으로 한 칸 옮김 
    if len(cursor): # 가장 왼쪽이면 무시
        save.append(cursor.pop())
def D(cursor): # 커서를 오른쪽으로 한 칸 옮김
    if len(save): # 가장 오른쪽이면 무시
        cursor.append(save.pop())
def B(cursor): # 커서 왼쪽 문자 삭제
    if len(cursor): # 가장 왼쪽이면 무시
     cursor.pop()
def P(a): # a라는 문자를 커서 왼왼쪽에 추가
    cursor.append(a)

    
cursor = list(map(str,sys.stdin.readline().strip()))
save = []
for _ in range(int(sys.stdin.readline().strip())):
    comm = sys.stdin.readline().split()
    if len(comm) == 1:
        if comm[0] == "L":
            L(cursor)
        if comm[0] == "D":
            D(cursor)
        if comm[0] == "B":
            B(cursor)
    else:
        P(comm[1])
while len(save) > 0: # 커서를 왼쪽으로 보내는 동안 pop했던 문자 복귀
    cursor.append(save.pop())

print("".join(cursor))