def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    maximum = 0
    for i in range(len(prices)-1):
        for j in range(i+1,len(prices)):
            if prices[j] - prices[i] > maximum:
                 maximum = prices[j] - prices[i]
    return maximum



prices = [7,6,4,3,1]
maxProfit(prices)
print("Done")