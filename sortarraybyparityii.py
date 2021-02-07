'''
922. Sort Array By Parity II
Given an array A of non-negative integers, half of the integers 
in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, 
i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.
'''
class Solution:
    def sortArrayByParityII(self, a):
        i = 0 # pointer for even misplaced
        j = 1 # pointer for odd misplaced
        sz = len(a)
        
        # invariant: for every misplaced odd there is misplaced even
        # since there is just enough space for odds and evens

        while i < sz and j < sz:
            if a[i] % 2 == 0:
                i += 2
            elif a[j] % 2 == 1:
                j += 2
            else:
                # a[i] % 2 == 1 AND a[j] % 2 == 0
                a[i],a[j] = a[j],a[i]
                i += 2
                j += 2

        return a
s=Solution()
print(s.sortArrayByParityII([4,5,2,7]))
print(s.sortArrayByParityII([4,6,8,9,2,5,7]))
