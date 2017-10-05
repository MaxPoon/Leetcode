from collections import deque
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]: return [[]]
        rows = len(matrix)
        cols = len(matrix[0])
        result = [[10000]*cols for _ in range(rows)]
        queue = deque()
        visited = set()
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    queue.append((row, col, 0))
                    visited.add((row, col))
        while queue:
            row, col, dist = queue.popleft()
            result[row][col] = dist
            for nextRow, nextCol in ((row+1, col), (row-1, col), (row, col+1), (row, col-1)):
                if (nextRow, nextCol) in visited: continue
                if nextRow < 0 or nextRow >= rows or nextCol < 0 or nextCol >= cols: continue
                queue.append((nextRow, nextCol, dist+1))
                visited.add((nextRow, nextCol))
        return result
