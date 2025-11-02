def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    from collections import Counter
    chars = Counter()
    left = right = 0
    res = 0
    while right < len(s):
        right_c = s[right]
        chars[right_c] += 1
        while chars[right_c] > 1: 
            left_c = s[left]
            chars[left_c] -= 1
            left += 1
        res = max[res, right - left + 1]
        right += 1
    return res