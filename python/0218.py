while(True):
    n = int(input())
    if not n: break
    for _ in range(n):
        m,e,j = map(int, input().split())
        if 100 in [m,e,j]: print("A"); continue
        elif (m+e)/2 >= 90: print("A"); continue
        elif (m+e+j)/3 >= 80: print("A"); continue
        elif (m+e+j)/3 >= 70: print("B"); continue
        elif (m+e+j)/3 >= 50 and (m>=80 or e>=80): print("B"); continue
        else: print("C"); continue