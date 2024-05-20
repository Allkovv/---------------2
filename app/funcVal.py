def on_off():
    global addp
    addp = True
    print("add on" ,addp)
    return addp

def test(func):
    global addp
    if func == True:
        print("YES", addp)
    else:
        print("NO", addp)

def off_on():
    global addp
    addp = False
    print("add off",addp)
    return addp

def del_on():
    global delp
    delp = True
    print("del", delp)
    return delp

def del_off():
    global delp
    delp = False
    print("Off del", delp)
    return delp
