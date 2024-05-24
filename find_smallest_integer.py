def find_smallest_int(arr):
    if (len(arr)==0):
        return 0

    ans = arr[0]
    for num in arr :
        if (num < ans):
            ans = num
    return ans

