def calculate_average(nums):
    if len(nums) == 0 :
        return 0
    total = sum(nums)
    count = len(nums)
    average = total / count
    return average

