while(True):
    try:
        s = input()
    except:
        break
    ec = dict([t,str(bin(i))[2:].zfill(5)] for i,t in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ .,-'?"))
    c = "".join(ec[e] for e in s)
    dc = {"101":" ","000000":"'","000011":",","10010001":"-","010001":".","000001":"?",
    "100101":"A","10011010":"B","0101":"C","0001":"D","110":"E","01001":"F",
    "10011011":"G","010000":"H","0111":"I","10011000":"J","0110":"K","00100":"L",
    "10011001":"M","10011110":"N","00101":"O","111":"P","10011111":"Q","1000":"R",
    "00110":"S","00111":"T","10011100":"U","10011101":"V","000010":"W","10010010":"X",
    "10010011":"Y","10010000":"Z"}
    ans = ""
    i=0
    while(i<len(c)):
        for j in range(3,9):
            try: ans += dc[c[i:i+j]]; i+=j; break
            except: continue
        else:
            break
    print(ans)
    