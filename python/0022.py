while(True):
    n = int(input())
    if n == 0:
        break
    r = -20000005
    s = 0
    for _ in range(n):
        a = int(input())
        s = max(a+s,a)
        r = max(r,s)
    print(r)
