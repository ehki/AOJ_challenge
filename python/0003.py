for _ in range(int(input())):
    a,b,c = sorted(list(map(int, input().split())))
    if c*c==a*a+b*b:
        print("YES")
    else :
        print("NO")