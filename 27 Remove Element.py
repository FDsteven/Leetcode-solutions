def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    new_list = [item for item in nums if item != val]
    return new_list

nums = [3,2,2,3]
val = 3
removeElement(nums, val)