
print("Hello World")
def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    output = []
    list_from_1 = nums1[:m]
    list_from_2 = nums2[:n]
    len_2 = len(list_from_2)
    # for i in list_from_1:
    #     if len_2 == 0:
    #         return list_from_1
    #     else:
    #         if list_from_2[0] < i:
    #             output.append(list_from_2[0])
    #             list_from_2 = list_from_2[1:]
    #             for j in list_from_2:
    #                 if j < i:
    #                     output.append(j)
    #                     list_from_2 = list_from_2[1:]
    #                 else:
    #                     break
    #             output.append(i)
    #         else:
    #             output.append(i)
    # if len_2 != 0:
    #     for final in list_from_2:
    #         output.append(final)
    output = list_from_1 + list_from_2
    output = [item for item in output if item != 0]
    output = sorted(output)


    return output
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3
merge(nums1,m,nums2,n)
print("Done")