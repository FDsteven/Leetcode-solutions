def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    for i in range(len(nums) - 1):
        for j in range(i + 1,min(i+k+1,len(nums))):
            if nums[i] == nums[j]:
                return True
    return False
            



nums = [1,2,3,1]
k = 3
nums = [1,0,1,1]
k = 1
nums = [1,2,3,1,2,3]
k = 2
print(containsNearbyDuplicate(nums, k))