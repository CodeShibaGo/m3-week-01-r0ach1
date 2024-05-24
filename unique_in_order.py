def unique_in_order(iterable):
    arr=[]
    for i,item in enumerate(iterable):
        if i == 0 or item != iterable[i-1]:
            arr.append(item)
    return arr


