while(True):
    try:
        N = int(input())
        m = 0
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    for l in range(10):
                        if i+j+k+l == N:
                            m += 1
        print(m)
    except:
        break