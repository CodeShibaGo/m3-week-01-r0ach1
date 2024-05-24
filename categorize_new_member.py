def categorize_new_member(data):
    ans =[]
    for member in data:
        a = member[0]
        b = member[1]
        if (a >= 55 and b >7):
            ans.append("Senior")
        else:
            ans.append("Open")
    return ans