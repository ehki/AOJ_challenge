while(True):
    try:
        a,c = input().split("=")
        a,b = a.split("+")
        for i in range(10):
            if i==0 and ((len(a)>1 and a[0]=="X") or (len(b)>1 and b[0]=="X") or (len(c)>1 and c[0]=="X")):
                continue
            if int(a.replace("X",str(i)))+int(b.replace("X",str(i))) == int(c.replace("X",str(i))):
                print(i)
                break
        else:
            print("NA")
    except:
        break