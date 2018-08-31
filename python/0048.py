while(True):
    try: s = float(input())
    except: break
    if 91.0<s : print("heavy"); continue
    if 81.0<s : print("light heavy"); continue
    if 75.0<s : print("middle"); continue
    if 69.0<s : print("light middle"); continue
    if 64.0<s : print("welter"); continue
    if 60.0<s : print("light welter"); continue
    if 57.0<s : print("light"); continue
    if 54.0<s : print("feather"); continue
    if 51.0<s : print("bantam"); continue
    if 48.0<s : print("fly"); continue
    print("light fly")