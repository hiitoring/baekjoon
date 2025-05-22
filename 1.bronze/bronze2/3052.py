nums = []
for i in range(10):
    a = int(input())
    na = a % 42
    nums.append(na)
    seta = set(nums)

print(len(seta))