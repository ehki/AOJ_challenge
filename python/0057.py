while(True):
    try: n = int(input())
    except: break
    print(1+sum([i+1 for i in range(n)]))