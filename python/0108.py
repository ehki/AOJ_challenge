while(int(input())):
    ar = list(map(int, input().split()))
    n = 0
    while(True):
        br = [ar.count(l) for l in ar]
        if ar == br:
            break
        ar = br
        n += 1
    print(n)
    print(" ".join(str(e) for e in br))
