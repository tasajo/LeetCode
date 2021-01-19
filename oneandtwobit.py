'''
717. 1-bit and 2-bit Characters
'''
class Solution(object):
    def isOneBitCharacter(self, bits):
        n = len(bits) - 1
        i = 0
        while i < n:
            i += 1 + bits[i]
        return i == n
s = Solution()
print(s.isOneBitCharacter([1,0,0]))
