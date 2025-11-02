def isValidSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    N = 9
    rows = [set() for _ in range(N)]
    columns = [set() for _ in range(N)]
    boxes = [set() for _ in range(N)]
    for row in range(N):
        for column in range(N):
            number = board[row][column]
            if number == ".":
                continue
            # check redundancy
            if number in rows[row]:
                return False
            if number in columns[column]:
                return False
            box_index = row//3 * 3 + column//3
            if number in boxes[box_index]:
                return False
            rows[row].add(number)
            columns[column].add(number)
            boxes[box_index].add(number)
    return True