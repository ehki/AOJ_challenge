dic = {}
while(True):
    try:
        key, page = input().split()
        page = int(page)
    except:
        break
    try:
        dic[key].append(page)
    except:
        dic[key] = [page]
a = list(dic.keys())
a.sort()
for b in a:
    print(b)
    print(" ".join(str(e) for e in sorted(dic[b])))
