def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    num_of_M = num_of_CM = num_of_D = num_of_CD = num_of_C = num_of_XC = num_of_L = num_of_XL = num_of_X = num_of_IX = num_of_V = num_of_IV = num_of_I = 0
    num_of_M,updated_num = divmod(num,1000)
    if updated_num >= 900:
        num_of_CM = 1
        updated_num -= 900
    num_of_D,updated_num = divmod(updated_num,500)
    if updated_num >= 400:
        num_of_CD = 1
        updated_num -= 400
    num_of_C, updated_num = divmod(updated_num,100)
    if updated_num >= 90:
        num_of_XC = 1
        updated_num -= 90
    num_of_L, updated_num = divmod(updated_num,50)
    if updated_num >= 40:
        num_of_XL = 1
        updated_num -= 40
    num_of_X, updated_num = divmod(updated_num,10)
    if updated_num >= 9:
        num_of_IX = 1
        updated_num -= 9
    num_of_V, updated_num = divmod(updated_num, 5)
    if updated_num >= 4:
        num_of_IV = 1
        updated_num -= 4
    num_of_I = updated_num
    output = "M" * num_of_M + "CM" * num_of_CM + "D" * num_of_D + "CD" * num_of_CD + "C" * num_of_C + "XC" * num_of_XC + "L" * num_of_L + "XL" * num_of_XL + "X" * num_of_X + "IX" * num_of_IX + "V" * num_of_V + "IV" * num_of_IV + "I" * num_of_I
    return output

print(intToRoman(994))