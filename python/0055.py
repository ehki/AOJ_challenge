while True:
    try: a = float(input())
    except: break
    ans = a
    for i in range(9):
        a = a*2*((i+1)&1)+a/3*(i&1)
        ans += a
    print("%.8f"%ans)