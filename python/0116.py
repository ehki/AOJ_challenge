from itertools import product
while(True):
    H,W = map(int,input().split())
    if not H: break
    ma = 0
    for i in range(H):
        ma |= (int(input().replace(".","0").replace("*","1"),2) << ((H-i-1)*W))
    flag = False
    hw = [[h,w] for h,w in product(range(H,0,-1),range(W,0,-1))]
    hw = sorted(hw,key=lambda x: -x[1]*x[0])
    ans = 0
    for h,w in hw:
        for i,j in product(range(H-h+1),range(W-w+1)):
            b = (sum([((2**w-1) << j) << k*W for k in range(h)]) ) << i*W
            c = ma&b
            if not c :flag = True; ans = max(ans,h*w); break
        else:
            continue
        if flag: break
    print(ans)
