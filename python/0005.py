import math
while(True):
    try:
        a,b = map(int, input().split())
        c = math.gcd(a,b)
        print(c, int(a*b/c))
    except:
        break
