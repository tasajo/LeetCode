'''
1266. Minimum Time Visiting All Points
'''
from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        x1, y1 = points.pop()
        while points:
            x2, y2 = points.pop()
            res += max(abs(y2 - y1), abs(x2-x1))
            x1, y1 = x2, y2
        return res

solution = Solution()
print(solution.minTimeToVisitAllPoints([[3,2],[-2,2]]))
print(solution.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
