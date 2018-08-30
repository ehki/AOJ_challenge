while(True):
    n = float(input())
    if n < 0: break
    if int(n*16)-n*16: print("NA"); continue
    else:
        s = bin(int(n*16))[2:].zfill(12)
        print(s[:-4]+"."+s[-4:])