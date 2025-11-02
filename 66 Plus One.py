def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    original_number = 0
    for i in range(len(digits)):
        original_number += (10**i * digits[-1-i])
    result_number = original_number + 1
    stash = []
    output = []
    while result_number > 0:
        result_number, digit =divmod(result_number,10)
        stash.append(digit)
    for i in range(len(stash)):
        top = stash.pop()
        output.append(top)
    return output

digits = [1,2,3]
digits = [4,3,2,1]
digits = [9]
print(plusOne(digits))