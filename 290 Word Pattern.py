def wordPattern(pattern, s):
    """
    :type pattern: str
    :type s: str
    :rtype: bool
    """
    map_word = {}
    map_pattern = {}
    s = s.split(" ")
    if len(s) != len(pattern):
        return False
    for p,w in zip(pattern,s):
        if p not in map_pattern:
            if w in map_word:
                return False
            else:
                map_word[w] = p
                map_pattern[p] = w
        else:
            if map_pattern[p] != w:
                return False

    return True
pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern, s))