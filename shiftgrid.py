"""
1260. Shift 2D Grid
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

    Element at grid[i][j] moves to grid[i][j + 1].
    Element at grid[i][n - 1] moves to grid[i + 1][0].
    Element at grid[m - 1][n - 1] moves to grid[0][0].

Return the 2D grid after applying shift operation k times.

Hints
Simulate step by step. move grid[i][j] to grid[i][j+1]. 
Handle last column of the grid.

Put the matrix row by row to a vector. 
Take k % vector.length and move last k of the vector to the beginning. 
Put the vector to the matrix back the same way.
"""

from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        start = m * n - k % (m * n)
        ans = []
        for i in range(start, m * n + start):
            j = i % (m * n)
            r, c = j // n, j % n
            if not (j - start) % n:
                ans.append([])
            ans[-1].append(grid[r][c])
        return ans

solution = Solution()
print("Example 1: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1")
print(solution.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 1))
print("\nExample 2: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4")
print(solution.shiftGrid([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], 4))
print("\nExample 3: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9")
print(solution.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 9))
