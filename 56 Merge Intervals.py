def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    intervals.sort(key=lambda x: x[0])
    output = []
    output.append(intervals[0])
    for i in range(1,len(intervals)):
        if intervals[i][0] <= output[-1][-1]:
            if intervals[i][-1] > output[-1][-1]:
                output[-1][-1] = intervals[i][-1]
        else:
            output.append(intervals[i])
    return output




intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,4],[4,5]]
# intervals = [[4,7],[1,4]]
print(merge(intervals))