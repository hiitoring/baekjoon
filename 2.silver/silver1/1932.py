n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int,input().split())))
if n > 1:
    triangle[1][0] += triangle[0][0]
    triangle[1][1] += triangle[0][0]
for i in range(2,n):
    for j in range(len(triangle[i])):
        if j == 0:
            triangle[i][j] += triangle[i-1][0]
        elif j == len(triangle[i])-1:
            triangle[i][j] += triangle[i-1][-1]
        else:
            triangle[i][j] += max(triangle[i-1][j],triangle[i-1][j-1])
print(max(triangle[n-1]))
