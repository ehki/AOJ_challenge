while(True):
    n = int(input())
    if not n: break
    a = [0]*10
    for _ in range(n):
        a[int(input())] += 1
    for b in a:
        print("*"*b if b else "-")