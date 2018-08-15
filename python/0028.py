from collections import Counter
a = []
while(True):
    try:
        a.append(int(input()))
    except:
        c = Counter(a)
        d = c.most_common()
        print("\n".join(str(e[0]) for e in d if e[1] == d[0][1]))
        break