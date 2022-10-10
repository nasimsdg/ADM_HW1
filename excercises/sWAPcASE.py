def swap_case(s):
    lst = list(s)
    st = str()
    for i in range(len(lst)):
        if lst[i].islower() == True:
            st = st + lst[i].upper()
        else:
            st = st + lst[i].lower()
    return st

