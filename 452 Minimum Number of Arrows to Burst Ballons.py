def findMinArrowShots(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    points.sort(key=lambda x: x[1])
    arrows = 1
    current = points[0]
    for i in range(1,len(points)):
        if points[i][0] > current[-1]:
            arrows += 1
            current = points[i]
    return arrows


points = [[10,16],[2,8],[1,6],[7,12]]
print(findMinArrowShots(points))