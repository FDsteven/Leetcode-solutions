def insert(intervals, newInterval):
    """
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """
    intervals.append(newInterval)
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
    intervals.sort(key = lambda x:x[0])
    left_bound = newInterval[0]
    right_bound = newInterval[1]
    i = 0
    if intervals[0][0] >= right_bound:
        if intervals[0][0] == right_bound:
            intervals[0][0] = left_bound
        else:
            intervals.append(newInterval)
        return intervals.sort(key =lambda x:x[0])
    while (i < len(intervals)) and (intervals[i][0] <= right_bound):
        if intervals[i][-1] <= left_bound:
            intervals[i][-1] = max(intervals[i][-1],right_bound)
        if intervals[i][0] >= left_bound:
            if intervals[i][0] <= right_bound:
                intervals[i][-1] = max(intervals[i][-1],intervals[i][1])
                intervals.pop(i)
        i += 1
    return intervals
            



intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(insert(intervals, newInterval))