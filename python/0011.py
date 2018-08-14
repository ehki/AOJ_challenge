w = int(input())
wa = list(range(w+1))
n = int(input())
for _ in range(n):
    a,b = map(int, input().split(","))
    wa[a],wa[b] = wa[b],wa[a]
for s in wa[1:]:
    print(s)
