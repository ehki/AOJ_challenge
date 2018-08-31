di = {"A":0,"B":0,"AB":0,"O":0}
while(True):
    try: di[input().split(",")[1]] += 1
    except: break
print(di["A"])
print(di["B"])
print(di["AB"])
print(di["O"])