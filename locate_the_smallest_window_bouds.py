def window(nums):
    left = right = None
    s = sorted(nums)
    for i in range(len(nums)):
        if nums[i] != s[i] and left == None:
            left = i
        elif nums[i] != s[i]:
            right = i
    return left,right

#The above takes o(n log n) because we sorted the array we can do better .

def update_solution_window(nums):
    min_num = float('inf')
    max_num = -float('inf')
    max_loc = min_loc = None
    for i in range(len(nums)):
        max_num = max(max_num,nums[i])
        if (max_num > nums[i]):
            max_loc = i
    for i in range(len(nums)-1,-1,-1):
        min_num = min(min_num,nums[i])
        if (min_num < nums[i]):
            min_loc = i
    return min_loc,max_loc
#The above function took o(n) time complexity;       



print(window([1,4,4,2,3,9,1,8,12,13,14]));
print(update_solution_window([1,4,4,2,3,9,1,8,12,13,14]));
