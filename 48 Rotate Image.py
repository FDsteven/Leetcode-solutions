def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    m = len(matrix)
    n = len(matrix[0])
    row = 0
    output = [[0]*m for _ in range(n)]
    while row < m:
        for index in range(n):
            output[index][m-row-1] = matrix[row][index]
        row += 1
    return output
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(rotate(matrix))
