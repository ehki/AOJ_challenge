while(True):
    n = int(input())
    if n == 0:
         break
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    arr = [ l+[sum(l)] for l in arr]
    brr = [0]*(n+1)
    for i in range(n):
        for j in range(n+1):
            brr[j] += arr[i][j]
    crr = arr+[brr]
    for c in crr:
        for d in c:
            print("%5d"%d,end="")
        print()