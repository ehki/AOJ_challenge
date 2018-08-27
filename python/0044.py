from math import sqrt, ceil

N = 53000
temp = [True]*(N+1)
temp[0] = temp[1] = False
for i in range(2, ceil(sqrt(N+1))):
    if temp[i]:
        temp[i+i::i] = [False]*(len(temp[i+i::i]))

while True:
    try:
        n = int(input())
        print(n-1-temp[n-1:0:-1].index(True), n+1+temp[n+1:].index(True))
    except EOFError: break