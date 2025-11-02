def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    output = []
    for i in range(len(nums)):
        item = nums[i]
        if item not in nums[:i]:
            output.append(nums[i])
    return output,len(output)
nums = [0,0,1,1,1,2,2,3,3,4]
removeDuplicates(nums)

print("Done")