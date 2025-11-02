def isIsomorphic(s, t):
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
    for i,j in zip(dict_s,dict_t):
        if dict_s[i] != dict_t[j]:
            return False
    return True

s = "egg"
t = "add"
s = "foo"
t = "bar"
s = "paper"
t = "title"
print(isIsomorphic(s, t))