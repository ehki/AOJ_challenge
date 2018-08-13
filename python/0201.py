# from pprint import pprint as pprint
import copy

def findrecipe(rec,ite,obj):
    # pprint(rec)
    # print("obj: ",obj)
    # print("=-")
    try:
        mat = rec[obj]
        rec2 = copy.copy(rec)
        del rec2[obj]
        price = min(ite[obj],sum([findrecipe(rec2,ite,m) for m in mat]))
        # print(price,obj)
        return price
    except:
        return ite[obj]

while(True):
    try:
        item = {}
        n = int(input())
        for _ in range(n):
            s,p = input().split()
            p = int(p)
            item[s] = p
        recipe = {}
        m = int(input())
        for _ in range(m):
            o,k,qs = input().split(" ",2)
            recipe[o] = qs.split()

        t = input()
        print(findrecipe(recipe,item,t))
    except:
        break