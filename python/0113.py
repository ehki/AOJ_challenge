while(True):
    checked = []
    try: p,q = map(int,input().split())
    except: break
    ansstr = ""
    while(True):
        p *= 10
        ans,p = p//q, p%q
        ansstr += str(ans)
        if p == 0:
            print(ansstr)
            break
        if p in checked:
            ansind = checked.index(p)
            print(ansstr)
            print(" "*ansind+"^"*(len(checked)-ansind))
            break
        else: checked.append(p)