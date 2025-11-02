import numpy as np
def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    cycle_length = numRows * 2 - 2
    num_of_columns = int(np.ceil(len(s) / cycle_length) * (numRows-1))
    output_matrix = [[" "] * num_of_columns for _ in range(numRows)]
    if numRows > 2:
        row_list = [item for item in range(numRows)]
        up_row_list = [numRows - 2 - item for item in range(numRows-2)]
        row_list = row_list + up_row_list
        column_list = [0] * numRows
        up_column_list = [item + 1 for item in range(numRows-2)]
        column_list = column_list + up_column_list
    else:
        row_list = [item for item in range(numRows)]
        column_list = [0] * numRows
    for i in range(len(s)):
        number_of_cycle,location = divmod(i,cycle_length)
        row = row_list[location]
        column_num = numRows - 1
        if numRows < 2:
            column_num = 1
        column = number_of_cycle * column_num + column_list[location]
        output_matrix[row][column] = s[i]
    output = ""
    for row in output_matrix:
        output += "".join(row)
    return output.replace(" ","")

s ="PAYPALISHIRING"
numRows = 4
print(convert(s, numRows))