'''
7. Reverse Integer
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer 
range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers 
(signed or unsigned).
'''

class Solution(object):
    def reverse(self, x):
        s = (x > 0) - (x < 0)
        r = int(str(x*s)[::-1])
        return s*r*(r<2**31)
        
solution = Solution()
print(solution.reverse(4393457))
print(solution.reverse(-1234))
print(solution.reverse(120))
print(solution.reverse(0))



