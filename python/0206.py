while(True):
    L = int(input())
    if not L:
        break
    a = 0
    b = 0
    c = 0
    for _ in range(12):
        a += 1
        M,N = map(int, input().split())
        b += M-N
        if not c and b >= L:
            c = a
    print(c if c else "NA")
