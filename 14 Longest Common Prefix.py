def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    output = ""
    first_string = strs[0]
    indi = 0
    for i in range(len(first_string)):
        letters = first_string[:i + 1]
        for item in strs:
            if letters != item[:i + 1]:
                return output
        output = letters

    return output