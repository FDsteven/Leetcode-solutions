def canCompleteCircuit(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    output = -1
    for i in range(len(gas)):
        for j in range(len(cost)):
            index = (i + j) % len(cost)
            if index >= i:
                i_slice = gas[i:index+1]
                j_slice = cost[i:index+1]
            else:
                i_slice = gas[i:] + gas[:index+1]
                j_slice = cost[i:] + cost[:index+1]
            if sum(i_slice) < sum(j_slice):
                break
            if j == len(cost) - 1:
                output = i
        
    return output
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
gas = [2,3,4]
cost = [3,4,3]
print(canCompleteCircuit(gas, cost))