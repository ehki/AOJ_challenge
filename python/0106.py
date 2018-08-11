p1,p2,p3 = 380,550,850
q1,q2,q3 = 200,300,500
d1,d2,d3 = 5,4,3
r1,r2,r3 = 0.2,0.15,0.12
arr = []
for tot in range(500,5001,100):
    lst = 1000000000
    for i in range(0,int(tot/q1)+1):
        for j in range(0,int(tot/q2)+1):
            for k in range(0,int(tot/q3)+1):
                if i*q1+j*q2+k*q3 == tot:
                    tmp = i*p1+j*p2+k*p3 - int(i/d1)*d1*p1*r1 - int(j/d2)*d2*p2*r2 - int(k/d3)*d3*p3*r3
                    lst = min(tmp,lst)
    arr.append([tot,int(lst)])
dic = dict(arr)
while(True):
    n = int(input())
    if n == 0:
        break
    print(dic[n])