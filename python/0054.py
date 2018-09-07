while(True):
    try: a,b,n = map(int, input().split())
    except: break
    print(sum(a*10**i//b%10 for i in range(1,n+1)))