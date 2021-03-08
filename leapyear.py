def code(x):
    if x %4 == 0:
        if x%400 ==0: 
            return True
        if x%100 ==0:
            return False
        else:
            return True
    return False