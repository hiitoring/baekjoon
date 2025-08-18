t = int(input())
for _ in range(t):
    n = int(input())
    sticker = []
    sticker.append(list(map(int,input().split())))
    sticker.append(list(map(int,input().split())))
    answer = list([0] * n for _ in range(3))
    answer[0][0] = 0
    answer[1][0] = sticker[1][0]
    answer[2][0] = sticker[0][0]
    
    for i in range(1,n):
        answer[0][i] = max(answer[0][i-1],answer[1][i-1],answer[2][i-1])
        answer[1][i] = max(answer[0][i-1] + sticker[1][i],answer[2][i-1] + sticker[1][i])
        answer[2][i] = max(answer[0][i-1] + sticker[0][i],answer[1][i-1] + sticker[0][i])
    print(max(answer[0][n-1],answer[1][n-1],answer[2][n-1]))