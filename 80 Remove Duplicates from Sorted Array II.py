def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    output = []
    for i in range(len(nums)):
        item = nums[i]
        list_slice = nums[:i]
        same_value_list = [elem for elem in list_slice if elem == item]
        number_of_occurences =  len(same_value_list)
        if number_of_occurences <= 1:
            output.append(nums[i])
    return output,len(output)

nums = [0,0,1,1,1,1,2,2,2,3,3,4,4]
removeDuplicates(nums)

print("Done")