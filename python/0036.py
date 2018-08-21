ans = [0,0,0,"C",0,0,0,0,"G","A","E",0,0,0,0,"D",0,"F",0,0,0,0,0,0,"B"]
while(True):
    h = ""
    for _ in range(8):
        h +=input()
    print(ans[h.rfind("1")-h.find("1")])
    try:
        b =input()
    except:
        break