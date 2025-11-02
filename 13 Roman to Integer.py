def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    output = 0
    separated_ist = [item for item in s]
    for i in separated_ist:
        if i == "I":
            output += 1
        if i == "V":
            output += 5
        if i == "X":
            output += 10
        if i == "L":
            output += 50
        if i == "C":
            output += 100
        if i == "D":
            output += 500
        if i == "M":
            output += 1000
    if "IV" in s:
        output -= 2
    if "IX" in s:
        output -= 2
    if "XL" in s:
        output -= 20
    if "XC" in s:
        output -= 20
    if "CD" in s:
        output -= 200
    if "CM" in s:
        output -= 200
    
    return output 