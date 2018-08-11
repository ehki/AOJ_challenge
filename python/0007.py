N = int(input())
a = 100000
for _ in range(N):
    a *= 1.05
    if a%1000:
        a -= a%1000
        a += 1000
print(int(a))