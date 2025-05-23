n = int(input())
nameli = set()
for i in range(n):
    name, status = input().split()
    if status == "enter":
        nameli.add(name)
    elif status == "leave":
        nameli.remove(name)
namelili = list(nameli)
namelili.sort(reverse=True)
for i in namelili:
    print(i)