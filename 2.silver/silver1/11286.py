n = int(input())
absnumli = []
numli = []
zeroli = []
count = 0
for i in range(n):
    num = int(input())
    if num != 0:
        numli.append(num)
    else:
        zeroli.append(num)
        count += 1
        if len(numli) < len(zeroli):
            numli.sort(key=lambda x: (abs(x), x))
            numli.append(0)
            for l in numli:
                print(l)
                numli = []
                zeroli = []
            
                    
                
