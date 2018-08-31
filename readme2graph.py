from matplotlib import pyplot as plt
import matplotlib as mpl
mpl.use('Agg')

di = {}
while(True):
    try: s = input()
    except: break
    if s[:3] == "## ":
        di[s[3:]] = 0
        while(True):
            try: n = input()
            except: break
            try:
                if n[0] == "`": di[s[3:]] += n[1:-3].count(" ")+1
                else: break
            except:
                break

plt.figure(figsize=(5,4),facecolor="W")
for k,v in sorted(di.items(), key=lambda x: -x[1]):
    plt.bar(k,v)
plt.savefig("num_solved_problems.png",dpi=200)
plt.close()