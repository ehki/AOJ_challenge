from sys import stdin

for _ in range(int(stdin.readline())):
    s = list(map(int, stdin.readline().split()))
    a = 0
    b = 0
    for c in s:
        if a<c: a=c
        elif b<c: b=c
        else:
            print("NO")
            break
    else:
        print("YES")
