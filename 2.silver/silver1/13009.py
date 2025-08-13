n = int(input())
zoo = list([1]*2 for _ in range(n+1))
zoo[1][0] = 2
for i in range(2,n+1):
    zoo[i][1] = (zoo[i-1][0] - zoo[i-1][1] + zoo[i][1]) % 9901
    zoo[i][0] = (zoo[i-1][0] + zoo[i][1] * 2) % 9901
print(zoo[n][0]+1 % 9901)