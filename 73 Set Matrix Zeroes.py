def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    m = len(matrix)
    n = len(matrix[0])
    output = [[0]*m for _ in range(n)]
    for row in range(m):
        for col in range(n):
            output[row][col] = matrix[row][col]
    row = 0
    while row < m:
        for column_idx in range(n):
            if matrix[row][column_idx] == 0:
                output[row] = [0 for _ in range(n)]
                for i in range(m):
                    output[i][column_idx] = 0
        row += 1
    return output
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(setZeroes(matrix))