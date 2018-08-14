ar = []
while(True):
    try:
        n = int(input())
        if n == 0:
            print(ar.pop())
        else:
            ar.append(n)
    except:
        break