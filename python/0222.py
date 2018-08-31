from math import sqrt, ceil

N = 10100000
temp = [True]*(N+1)
temp[0] = temp[1] = False
for i in range(2, ceil(sqrt(N+1))):
    if temp[i]:
        temp[i+i::i] = [False]*(len(temp[i+i::i]))

quadruplet = [True, False, True, False, False, False, True, False,True]
while True:
    try: n = int(input())
    except: break
    for i in range(n,9,-1):
        if temp[i] and temp[i-8:i+1] == quadruplet:
            print(i)
            break
