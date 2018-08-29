while(True):
    n = int(input())
    if n == -1: break
    p = 1150
    if   n < 10: print(4280-p)
    elif n < 20: p += 125*(n-10); print(4280-p)
    elif n < 30: p += 125*10; p += 140*(n-20); print(4280-p)
    else: p += 125*10; p += 140*10; p += 160*(n-30); print(4280-p)
