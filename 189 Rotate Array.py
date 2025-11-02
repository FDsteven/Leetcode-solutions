def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    new_list = nums.copy()
    for i in range(len(nums)):
        index = (k+i)%len(nums)
        new_list[index] = nums[i]
    return new_list


nums = [-1,-100,3,99]
k = 2
new_list = nums.copy()
for i in range(len(nums)):
    index = (k+i)%len(nums)
    new_list[index] = nums[i]
rotate(nums, k)