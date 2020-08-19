def smallest_count_naive(nums):
    result = []
    for i,num in enumerate(nums):
        result.append(sum(val < num for val in nums[i+1:]))
        print(sum(val < num for val in nums[i+1:]))
    return result


print(smallest_count_naive([3,4,9,6,1]));
