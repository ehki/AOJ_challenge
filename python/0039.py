dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

while(True):
    try:
        lis = list(input())
        ans = [dic[e] for e in lis]
        print(sum([-ans[i] if ans[i]<ans[i+1] else ans[i] for i in range(len(ans)-1)] + [ans[-1]]))
    except:
        break