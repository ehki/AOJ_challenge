memo = [0]*20010
lidx = 1

def solve(m):
    global lidx,memo
    if m < lidx: return memo[m]
    for i in range(lidx,m+1):
        memo[i] = memo[i-1]
        n = i
        while n%5 == 0:
            n/=5
            memo[i] += 1
    lidx = m
    return memo[m]


while(True):
    n = int(input())
    if not n: break
    print(solve(n))
