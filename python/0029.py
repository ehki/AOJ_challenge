from collections import Counter
s = list(input().split())
c = Counter(s)
n,m = 0,0
for e in s:
    if n < len(e):
        n = len(e)
        m = e
print(c.most_common()[0][0],m)
