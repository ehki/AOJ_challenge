k = [[1,2,4,8],[4,8,1,2],[8,1,2,4],[2,4,8,1]]
m = [[0]*5 for _ in range(5)]

for i in range(9):
    a = input()
    if i%2:
        for j in range(5):
            if a[j] == '1':
                m[i//2][j] |= 4
                m[i//2+1][j] |= 1
    else:
        for j in range(4):
            if a[j] == '1':
                m[i//2][j] |= 2
                m[i//2][j+1] |= 8
y,x,direct = 0,0,0
ans = []
while True:
    for i in range(4):
        if m[y][x] & k[direct][i]:
            d = k[direct][i]
            if   d == 1: y -= 1; direct = 2
            elif d == 2: x += 1; direct = 0
            elif d == 4: y += 1; direct = 3
            else       : x -= 1; direct = 1
            ans.append(direct)
            break
    if not ( x or y ): break
print("".join("RLUD"[e] for e in ans))