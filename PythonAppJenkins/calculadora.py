def conversor(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return str(value)

def add(arg1,arg2):
    argconv1 = conversor(arg1)
    argconv2 = conversor(arg2)

    if isinstance(argconv1,str) or isinstance(argconv2,str):
        argconv1 =str(argconv1)
        argconv2 =str(argconv2)
    return argconv1 + argconv2