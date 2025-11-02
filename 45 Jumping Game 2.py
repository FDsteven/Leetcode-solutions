def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) == 1: return 0
    last = next = 0
    count = 1
    for i in range(len(nums)):
        temp = next
        next = max(nums[j]+j for j in range(last, next+1))
        if next >= len(nums)-1:
            break
        count += 1
        last = temp
    return count

nums = [2,3,1,1,4]
print(canJump(nums))
nums = [2,3,0,1,4]
print(canJump(nums))