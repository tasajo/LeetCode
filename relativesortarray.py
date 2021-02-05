'''
1122. Relative Sort Array
Given two arrays arr1 and arr2, the elements of arr2 are distinct, 
and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in 
arr1 are the same as in arr2.  Elements that don't appear in arr2 should 
be placed at the end of arr1 in ascending order.
'''

import collections

class Solution:
    def relativeSortArray(self, arr1, arr2):
        c = collections.Counter(arr1)
        res = []       
        for i in arr2:
            res += [i]*c.pop(i)  
        return res + sorted(c.elements())

s = Solution()
print(s.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))
# Expected: [2,2,2,1,4,3,3,9,6,7,19]
