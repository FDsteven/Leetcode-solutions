def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    output = -1
    needlelist = haystack.split(needle)
    if len(needlelist) > 1:
        output = len(needlelist[0])
    return output
haystack = "leetcode"
needle = "leeto"
print(strStr(haystack, needle))