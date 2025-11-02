def minSubArrayLen(target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    window_size = 1
    while window_size < len(nums):
        for i in range(len(nums)-window_size + 1):
            if sum(nums[i:i+window_size]) >= target:
                return window_size
        window_size += 1
    return 0
target = 11
nums = [1,1,1,1,1,1,1,1]
print(minSubArrayLen(target, nums))