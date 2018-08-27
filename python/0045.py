n = 0
sum = 0
ave = 0
while(True):
    try:
        a,b = map(int,input().split(","))
        sum += a*b
        ave += b
        n += 1
    except EOFError:
        print(sum)
        print(int(ave/n+0.5))
        break