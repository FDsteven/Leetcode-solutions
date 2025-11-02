def candy(ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """
    output = [1] * len(ratings)
    for i in range(len(ratings)-1):
        if ratings[i] > ratings[i+1]:
            output[i] += 1
        if ratings[i+1] > ratings [i]:
            output[i + 1] += 1
    return output, sum(output)
ratings = [100, 80, 70, 60, 70, 80, 90, 100, 90, 80, 70, 60, 60]
print(candy(ratings))
