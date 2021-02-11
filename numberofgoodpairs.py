"""
1512. Number of Good Pairs

Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.
"""
from typing import List

class Solution:
        # search for duplicate numbers
        def numIdenticalPairs(self, nums: List[int]) -> int:
        
            # number of good pairs
            repeat = {}
            num = 0

            # for every element in nums
            for v in nums:

                # number of repeated digits
                if v in repeat:

                    # count number of pairs based on duplicate values
                    if repeat[v] == 1:
                        num += 1
                    else:
                        num += repeat[v]

                    # increment the number of counts
                    repeat[v] += 1
                # number has not been seen before
                else:
                    repeat[v] = 1
            # return
            return num

s = Solution()
print(s.numIdenticalPairs([1,2,3,1,1,3]))

"""
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
"""
