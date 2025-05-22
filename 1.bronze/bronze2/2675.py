T = int(input())
for i in range(T):
    sums=""
    R, s = input().split()
    inr = int(R)
    slen = len(s)
    for n in range(slen):
        sums += (s[n]*inr)
    print(sums)

