while(True):
    try:
        v = float(input())
        print(int((4.9*(v/9.8)**2)/5)+2)
    except:
        break
