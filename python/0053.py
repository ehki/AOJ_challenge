from math import sqrt, ceil
from itertools import accumulate
N = 120000
temp = [True]*(N+1)
temp[0] = temp[1] = False
for i in range(2, ceil(sqrt(N+1))):
    if temp[i]:
        temp[i+i::i] = [False]*(len(temp[i+i::i]))

cumsum = [i for i in range(N) if temp[i]]
cumsum = list(accumulate(cumsum))
while True:
    n = int(input())
    if not n: break
    print(cumsum[n-1])