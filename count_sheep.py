def count_sheep(sheep):
    if (len(sheep)==0):
        return 0

    count = 0
    for s in sheep:
        if (s == True):
            count +=1
    return count



