def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    boolean = [0] * len(nums)
    output = True
    for i in range(len(nums)):
        boolean[i] = 1 if nums[i] != 0 else 0
    for i in range(len(nums)):
        if boolean[i] == 0:
            nums_slice = nums[:i]
            indi = [0] * i
            for j in range(i):
                if nums_slice[j] > (i-j):
                    indi[j] = 1
            if sum(indi)>0:
                output = True
            else:
                output = False
    return output

nums = [2,3,1,1,4]
print(canJump(nums))
nums = [3,2,1,0,4]
print(canJump(nums))