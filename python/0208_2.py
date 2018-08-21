from sys import stdin
while(True):
    n = int(stdin.readline())
    if not n:
        break
    print(str(oct(n))[2:].translate(str.maketrans('4567','5789')))
