def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    


nums = [2,2,1,1,1,2,2]
unique_items = []
for i in range(len(nums)):
    if nums[i] not in unique_items:
        unique_items.append(nums[i])
for i in unique_items:
    slice_list = [item for item in nums if item == i]
    if len(slice_list) >= 0.5 * len(nums):
        print(i)
print("Done")