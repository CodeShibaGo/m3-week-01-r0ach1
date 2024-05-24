def distinct(seq):
    seen = set()  # 用來追蹤已經見過的元素
    re = []  # 用來存放不重複的元素，保留原始順序

    for x in seq:
        if x not in seen:  # 如果 x 還沒見過
            seen.add(x)  # 將 x 加入已見過的集合
            re.append(x)  # 將 x 添加列表
    return re
