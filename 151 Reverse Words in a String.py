def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    s = s.strip()
    strs = s.split(' ')
    while " " in strs:
        strs.remove(" ")
    output = ""
    for i in range(len(strs)):
        insert = strs[-i - 1].strip()
        if len(insert) > 0:
            output += insert
            output += " "
    output = output[:len(output)-1]
    return output
