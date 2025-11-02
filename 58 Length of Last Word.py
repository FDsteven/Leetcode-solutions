def lengthOfLastWord(self, s):
    """
    :type s: str
    :rtype: int
    """
    s = s.rstrip()
    s_list = s.split(" ")
    return len(s_list[-1])