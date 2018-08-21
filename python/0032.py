from sys import stdin

na = 0
nb = 0
while(True):
    try:
        a,b,c = map(int,stdin.readline().split(","))
        if a**2+b**2==c**2:
            na += 1
        if a==b:
            nb += 1
    except:
        break
print(na)
print(nb)