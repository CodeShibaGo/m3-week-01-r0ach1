def age_difference(ages):
    min = ages[0]
    max = ages[0]

    for age in ages:
        if (age > max):
            max = age
        elif (age < min):
            min = age #順序不能對調
    return (min, max)