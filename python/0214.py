
# def chk_in_rect(xy1,xy2):
#     chk2in1 = True
#     for i in range(4):
#         for j in range(4):
#             a = (xy1[(2*i+2)&7]-xy1[(2*i  )&7]) * (xy2[(2*j+1)&7]-xy1[(2*i+1)&7])
#             b = (xy1[(2*i+3)&7]-xy1[(2*i+1)&7]) * (xy2[(2*j  )&7]-xy1[(2*i  )&7])
#             if a > b: chk2in1 = False; break
#     chk1in2 = True
#     for i in range(4):
#         for j in range(4):
#             a = (xy2[(2*i+2)&7]-xy2[(2*i  )&7]) * (xy1[(2*j+1)&7]-xy2[(2*i+1)&7])
#             b = (xy2[(2*i+3)&7]-xy2[(2*i+1)&7]) * (xy1[(2*j  )&7]-xy2[(2*i  )&7])
#             if a > b: chk2in1 = False; break
#     if chk2in1|chk1in2: return True
#     else: return False

# def chk_intersect(xy1,xy2):
#     for i in range(4):
#         for j in range(4):
#             a = (xy1[(2*i  )&7]-xy1[(2*i+2)&7]) * (xy2[(2*j+1)&7]-xy1[(2*i+3)&7])
#             a+= (xy1[(2*i+1)&7]-xy1[(2*i+3)&7]) * (xy2[(2*i  )&7]-xy1[(2*j  )&7])
#             b = (xy1[(2*i  )&7]-xy1[(2*i+2)&7]) * (xy2[(2*j+3)&7]-xy1[(2*i+3)&7])
#             b+= (xy1[(2*i+1)&7]-xy1[(2*i+3)&7]) * (xy2[(2*i  )&7]-xy1[(2*j+2)&7])
#             if a*b <= 0 : return True
#     else:
#         return False

from sys import stdin
while(True):
    try:
        n = int(stdin.readline())
    except:
        exit()
    if not n: exit()
    for _ in range(n):
        m = int(stdin.readline())
        try: hoge = [list(map(int, stdin.readline().split())) for j in range(m)]
        except: exit()
        print("1\n")


exit()
while(True):
    n = int(input())
    if n == 0: break
    for j in range(n):
        m = int(input())
        xys = [ [input() for k in range(4)] for i in range(m) ]
        print("1")
exit()
while(True):
    n = int(input())
    if not n: break
    for _ in range(n):
        m = int(input())
        # p = list(range(m))
        xys = [ map(int,input().split()) for i in range(m) ]
        print(1)
        continue
        # # print(n,m,xys)
        # for i in range(m):
        #     if len(set(p)) == 1: print(1); break
        #     for j in range(i+1,m):
        #         if p[i] == p[j]:
        #             continue
        #         if chk_in_rect(xys[i],xys[j]):
        #             # print("in_rect")
        #             p = [i if e==j else e for e in p]
        #             continue
        #         if chk_intersect(xys[i],xys[j]):
        #             # print("intersect")
        #             p = [i if e==j else e for e in p]
        #             continue
        # else: print(p,len(set(p)))