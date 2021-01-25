"""Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings."""

class Solution:
    def __init__(self):
        pass
        
    def balancedStringSplit(self, s: str) -> int:
        res = cnt = 0
        for c in s:
            cnt += 1 if c == 'L' else -1
            if cnt == 0:
                res += 1
        return res

solution = Solution()
print(solution.balancedStringSplit("LLLLRRRR"))



"""
Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", 
each substring contains same number of 'L' and 'R'.

Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", 
each substring contains same number of 'L' and 'R'.

Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".

Example 4:

Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", 
since each substring contains an equal number of 'L' and 'R'
"""
