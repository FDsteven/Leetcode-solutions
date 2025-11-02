def hIndex(citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    for i in range(len(citations)):
        cit_slice = [item for item in citations if item > i]
        if len(cit_slice) < i + 1:
            return i


citations = [3,0,6,1,5]
citations = [1,3,1]
print(hIndex(citations))