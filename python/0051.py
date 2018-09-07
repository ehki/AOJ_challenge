n = int(input())
for _ in range(n):
    s = list(input())
    mins = "".join(sorted(s,reverse=False))
    maxs = "".join(sorted(s,reverse=True))
    print(int(maxs)-int(mins))