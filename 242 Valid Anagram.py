def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    from collections import Counter
    dict_s = Counter(s)
    dict_t = Counter(t)
    if len(dict_s) != len(dict_t):
        return False
    dict_s = dict(sorted(dict_s.items(), key=lambda item: item[1]))
    dict_t = dict(sorted(dict_t.items(), key=lambda item: item[1]))
    if dict_s == dict_t:
        return True
    else:
        return False
    
s = "anagram"
t = "nagaram"
s = "rat"
t = "car"
print(isAnagram(s, t))