while(True):
    try: p,q = map(int,input().split())
    except: break
    ansstr = ""
    checked = [p%q]
    while(True):
        ans,p = divmod(p*10,q)
        ansstr += str(ans)
        if p == 0:
            print(ansstr)
            break
        if p in checked:
            ansind = checked.index(p)
            print(ansstr)
            print(" "*(ansind)+"^"*(len(checked)-ansind))
            break
        else: checked.append(p)
