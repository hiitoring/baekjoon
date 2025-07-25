def default():
        hap[1][1] = 1
        hap[2][2] = 1
        hap[3][1] = 1 
        hap[3][2] = 1
        hap[3][3] = 1

t= int(input())
n = [int(input()) for _ in range(t)]
maxn = max(n)
hap=[]
for i in range(0,maxn+1):
    hap.append([0]*4)
    if i == 3:
        default()
    elif i > 3 :
        hap[i][1] = (hap[i-1][2] + hap[i-1][3]) % 1000000009
        hap[i][2] = (hap[i-2][1] + hap[i-2][3]) % 1000000009
        hap[i][3] = (hap[i-3][1] + hap[i-3][2]) % 1000000009

for j in n:
      print(sum(hap[j])%1000000009)
    
