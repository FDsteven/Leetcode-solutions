def summaryRanges(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    from collections import Counter
    num_dict = Counter(nums)
    output = []
    for i in num_dict.keys():
        if i - 1 not in num_dict:
            string = str(i)
            j = i
            while j in num_dict:
                temp = j
                j += 1
            string = string + "->" + str(temp) if temp != i else string
            output.append(string)
    return output

nums = [0,1,2,4,5,7]
nums = [0,2,3,4,6,8,9]
nums = [5,8]
print(summaryRanges(nums))