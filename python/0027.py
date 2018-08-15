while(True):
    m,d = map(int,input().split())
    if m==0 and d==0:
        break
    dn = sum([[31,29,31,30,31,30,31,31,30,31,30,31][a] for a in range(m-1)]) + d-1
    print(["Thursday","Friday","Saturday","Sunday","Monday","Tuesday","Wednesday"][dn%7])