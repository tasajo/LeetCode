'''415. Add Strings
'''
class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        nums1 = list(num1)
        nums2 = list(num2)
        res, carry = [], 0

        while nums1 or nums2:
            n1 = n2 = 0
            if nums1: n1 = ord(nums1.pop()) - ord('0')
            if nums2: n2 = ord(nums2.pop()) - ord('0')
            
            carry, remain = divmod(n1 + n2 + carry, 10)
            res.append(remain)
        
        if carry:
            res.append(carry)
        return ''.join(str(d) for d in res)[::-1]
        
s = Solution()
print(s.addStrings('10','20'))
