from collections import Counter

ans = ["null","one pair","two pair","three card","straight","full house","four card"]
straits = [[i,i+1,i+2,i+3,i+4]for i in range(1,10)]
straits.append([1,10,11,12,13])

while(True):
    try:
        l = sorted(list(map(int,input().split(","))))
        v = sorted(list(Counter(l).values()))
        p = 0
        if v == [1,1,1,2]: p = 1
        elif v == [1,2,2]: p = 2
        elif v == [1,1,3]: p = 3
        elif l in straits: p = 4
        elif v == [2,3]: p = 5
        elif v == [1,4]: p = 6
        print(ans[p])
    except:
        break