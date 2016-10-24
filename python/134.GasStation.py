class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        l = len(gas)
        i=0
        while i<l:
            j=i
            totalGas, totalCost = 0,0
            pass0=False
            while True:
                totalGas+=gas[j]
                totalCost+=cost[j]
                if totalCost>totalGas:
                    break
                j+=1
                if j>=l:
                    j-=l
                    pass0=True
                if j==i:
                    return i
            if pass0:
                break
            i=j+1
        return -1