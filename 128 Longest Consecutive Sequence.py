def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    from collections import Counter
    nums.sort()
    num_dict = Counter(nums)
    output = 0
    for i in num_dict.keys():
        if i - 1 not in num_dict:
            length = 1
            j = i + 1
            while j in num_dict:
                length += 1
                j += 1
            output = max(output,length)
    return output
    


nums = [0,3,7,2,5,8,4,6,0,1]
nums = [100,4,200,1,3,2]
nums = [1,0,1,2]
print(longestConsecutive(nums))