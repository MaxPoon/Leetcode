class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stoneSet = set(stones)
        lastStone = stones[-1]
        if stones[1] != 1: return False
        if len(stones) == 2: return True
        if lastStone > stones[-2] + len(stones): return False
        visited = set()
        def canCrossRecursive(position, jump):
            for nextJump in jump + 1, jump, jump - 1:
                if nextJump < 1: continue
                nextPosition = nextJump + position
                if nextPosition == lastStone: return True
                if nextPosition not in stoneSet: continue
                if (nextPosition, nextJump) in visited: continue
                if canCrossRecursive(nextPosition, nextJump): return True
                else: visited.add((nextPosition, nextJump))
            return False
        return canCrossRecursive(1, 1)
        