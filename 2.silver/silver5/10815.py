n = int(input())
nums = set(map(int,input().split()))
m = int(input())
nums2 = list(map(int,input().split()))
for i in range(m):
    if nums2[i] in nums :
        nums2[i] = str(1)
    else:
        nums2[i] = str(0)
joinnums2 = " ".join(nums2)
print(joinnums2)