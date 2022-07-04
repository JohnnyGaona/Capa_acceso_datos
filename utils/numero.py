
def numero(x):
    if x.isnumeric():
        if len(x) == 10:
            return True
        else:
            return False
    else:
        return False