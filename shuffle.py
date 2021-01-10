# 1470. Shuffle the Array
from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.extend([nums[i], nums[i+n]])
        return res
    
    example = [1,3,5,7,9,11,15,19]
    print(example)
    print(shuffle("nums", example, 4))

