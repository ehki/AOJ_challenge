n = int(input())
for _ in range(n):
    s1 = int(input())
    s2 = int(input())
    s3 = s1+s2
    if len(str(s3)) > 80:
        print("overflow")
    else:
        print(s3)