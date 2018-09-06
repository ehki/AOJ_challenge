from heapq import heappush, heappop
rot1 = [1,2,3,4,5,6,22,23,24,12,11,10,18,14,15,16,17,13,19,20,21,7,8,9,25,26,27,28,29,30]
rot2 = [28,29,30,4,5,6,7,8,9,10,11,12,13,14,16,15,17,18,21,20,19,22,23,24,25,26,27,1,2,3]
rot3 = [24,2,3,27,5,6,30,8,9,21,11,12,13,14,15,18,17,16,19,20,10,22,23,1,25,26,4,28,29,7]
rot4 = [1,2,22,4,5,25,7,8,28,10,11,19,15,14,13,16,17,18,12,20,21,3,23,24,6,26,27,9,29,30]
N = int(input())
for _ in range(N):
    closeset = set()
    finstate = (1,1,1,1,1,1,1,1,1,2,2,2,4,4,4,6,6,6,5,5,5,3,3,3,3,3,3,3,3,3)
    state = tuple(map(int,input().split()))
    que = [(0,state,0)]
    while que:
        numope, cstate, lasope = heappop(que)
        if cstate == finstate: break
        if cstate in closeset: continue
        closeset.add(cstate)
        for ope,rot in zip(range(1,5),[rot1,rot2,rot3,rot4]):
            if lasope != ope:
                nstate = tuple(cstate[i-1] for i in rot)
                heappush(que,(numope+1,nstate,ope))
    print(numope)