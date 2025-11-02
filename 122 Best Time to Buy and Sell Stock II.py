def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    maximum = 0
    price_diff = [] # index is for +1
    plusminus = [] # index is for +1
    for i in range(len(prices)-1):
        price_diff.append(prices[i+1] - prices[i])
        if price_diff[i] < 0:
            plusminus.append(-1)
        else:
            plusminus.append(1)
    if sum(plusminus) == len(plusminus) * (-1):
        print(maximum)
    else:
        profit = [item for item in price_diff if item > 0]
        maximum = sum(profit)

        
   
    return maximum

prices = [7,1,5,3,6,4]
# prices = [1,2,3,4,5]
# prices = [7,6,4,3,1]
maximum = 0
price_diff = [] # index is for +1
plusminus = [] # index is for +1
buypoint = 0
sell_points = [0] * len(prices) # index is for +2
buy_point = [0] * len(prices)
for i in range(len(prices)-1):
    price_diff.append(prices[i+1] - prices[i])
    if price_diff[i] < 0:
        plusminus.append(-1)
    else:
        plusminus.append(1)
if sum(plusminus) == len(plusminus) * (-1):
    print(maximum)
else:
    profit = [item for item in price_diff if item > 0]
    maximum = sum(profit)

print("Done")