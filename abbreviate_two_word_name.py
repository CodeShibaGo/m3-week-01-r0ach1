def abbrev_name(name):
  first_name, last_name = name.split()
  #split 不指定字符會根據空格切割字串

  first_initial = first_name[0].upper()
  last_initial = last_name[0].upper()
  return f"{first_initial}.{last_initial}"
