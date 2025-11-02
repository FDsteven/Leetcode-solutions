def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    output = []
    rows = len(matrix)
    columns = len(matrix[0])
    up = left = 0
    right = columns - 1
    down = rows - 1
    while len(output) < rows * columns:
        for col in range(left, right + 1):
            output.append(matrix[up][col])
        for row in range(up + 1, down + 1):
            output.append(matrix[row][right])
        if up != down:
            for col in range(right - 1, left - 1, -1):
                output.append(matrix[down][col])
        if left != right:
            for row in range(down - 1, up, -1):
                output.append(matrix[row][left])
        left += 1
        right -= 1
        up += 1
        down -= 1
    return output

matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix))