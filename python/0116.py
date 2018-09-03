# ref: http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=924554#1
from itertools import product
while(True):
    H,W = map(int,input().split())
    if not H: break
    ma = [list(map(int,input().replace(".","1").replace("*","0")))+[0] for _ in range(H)]
    for i,j in product(range(1,H),range(W)):
        if ma[i][j]: ma[i][j] += ma[i-1][j]
    ans = 0
    for i in range(H):
        stk = []
        for j in range(W+1):
            cur = ma[i][j]
            if (not stk) or stk[-1][1] < cur:
                stk.append([j,cur])
            elif stk[-1][1] > cur:
                idx = j
                while stk and stk[-1][1] >= cur:
                    idx = stk[-1][0]
                    ans = max(ans,stk[-1][1]*(j-stk[-1][0]))
                    stk.pop()
                stk.append([idx,cur])
    print(ans)