class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if len(stones) == 2:  return stones[1] == 1
        n = len(stones)
        val2id = {stone: i for i, stone in enumerate(stones)}
        dp = collections.defaultdict(set)
        dp[1].add(0)
        for j in range(1, n):
            for i in dp[j]:
                step = stones[j] - stones[i]
                for k in [step + 1, step, step - 1]:
                    _next = stones[j] + k
                    _next = val2id.get(_next, j)
                    if _next != j:
                        if _next == n - 1:
                            return True
                        dp[_next].add(j)
 
        return False
