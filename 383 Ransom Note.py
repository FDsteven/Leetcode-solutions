def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    from collections import Counter
    output = True
    dict_magazine = Counter(magazine)
    for i in range(len(ransomNote)):
        char = ransomNote[i]
        if char in dict_magazine:
            dict_magazine[char] -= 1
            if dict_magazine[char] < 0:
                return False
        else:
            return False

    return output
ransomNote = "aa"
magazine = "aab"
ransomNote = "aa"
magazine = "ab"
ransomNote = "a"
magazine = "b"
print(canConstruct(ransomNote, magazine))