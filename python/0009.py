from math import sqrt, ceil

N = 1000000
temp = [True]*(N+1)
temp[0] = temp[1] = False
for i in range(2, ceil(sqrt(N+1))):
    if temp[i]:
        temp[i+i::i] = [False]*(len(temp[i+i::i]))

while True:
    try:print(len([1 for _ in temp[:int(input())+1] if _]))
    except:break