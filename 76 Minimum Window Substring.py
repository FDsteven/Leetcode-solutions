
def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    from collections import Counter
    if not t or not s:
        return ""
    dict_t = Counter(t)
    required = len(dict_t)
    formed = 0
    left = 0
    right = 0
    window_counts = {}
    output = float('inf'), None, None
    while right < len(s):
        character = s[right]
        window_counts[character] = window_counts.get(character,0) + 1
        if (character in dict_t) and (window_counts[character] == dict_t[character]):
            formed += 1
        while left <= right and formed == required:
            character = s[left]
            if right - left + 1< output[0]:
                output = (right - left + 1, left, right)
            window_counts[character] -= 1
            if (character in dict_t) and (window_counts[character] < dict_t[character]):
                formed -= 1
            left += 1
        right += 1
        
    return "" if output[0] == float('inf') else s[output[1] : output[2] + 1]

s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))