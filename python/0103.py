n = int(input())
for i in range(n):
    no = 0
    np = 0
    tm = 0
    while(True):
        s = input()
        if s == "HIT":
            tm += 1
            if tm >= 4:
                np += 1
                tm = 3
        if s == "HOMERUN":
            np += tm +1
            tm = 0
        if s == "OUT":
            no += 1
        if no >= 3:
            print(np)
            break