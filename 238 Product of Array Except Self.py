def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    output = []
    for i in range(len(nums)):
        temp = [item for item in nums]
        del temp[i]
        initial = 1
        for j in range(len(temp)):
            initial = initial * temp[j]
        output.append(initial)
    return output
nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))