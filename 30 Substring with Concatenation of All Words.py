def findSubstring(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    left = 0
    increment = len(words[0])
    num_of_words = len(words)
    right = num_of_words * increment
    output = []
    while right <= len(s):
        words_copy = [item for item in words]
        if s[left:left+increment] in words_copy:
            jumps = 1
            words_copy.remove(s[left:left+increment])
            while jumps < num_of_words:
                if s[left + increment * jumps:left + increment * (jumps+1)] not in words_copy:
                    break
                else:
                    words_copy.remove(s[left + increment * jumps:left + increment * (jumps+1)])
                    jumps += 1
            if len(words_copy) == 0:
                output.append(left)
        right += 1
        left += 1
    return output
s = "barfoothefoobarman"
words = ["foo","bar"]
# s = "wordgoodgoodgoodbestword"
# words = ["word","good","best","word"]
s ="wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
print(findSubstring(s, words))

                
