t = int(input())
nums = []
plusminus = []
i = 0
for _ in range(t):
    n = int(input())
    if n > i: # 입력 받은 수가 마지막으로 입력한 수보다 크다면 push
        for i in range(i+1,n+1): 
            nums.append(i)
            plusminus.append("+")
    if nums[-1] == n: # 리스트의 마지막 수가 n과 같다면 pop
       nums.pop()
       plusminus.append("-")
    else:
        print("NO")
        break
if len(nums) == 0: # 리스트가 모두 pop 되었다면 print
    for j in plusminus:
        print(j)

