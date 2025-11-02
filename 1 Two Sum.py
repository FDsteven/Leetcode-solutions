def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    import collections
    ans = collections.defaultdict(list)
    for i in range(len(nums)):
        ans[nums[i]].append(i)
    for i in nums:
        if target - i in ans:
            if (target - i == i):
                if (len(ans[i]) > 1):
                    return [ans[i][0],ans[target - i][1]]
            else:
                return [ans[i][0],ans[target - i][0]]
            


nums = [2,7,11,15]
target = 9
nums = [3,2,4]
target = 6
print(twoSum(nums, target))