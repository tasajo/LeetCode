# 1480. Running Sum of 1d Array

from typing import List

class Solution:
    def runningSum(self, numslist: List[int]) -> List[int]:
        sum = 0
        result = []
        for i in range(len(numslist)):
            sum += numslist[i]
            result.append(sum)
        return result
    
    example = list([4,3,4,5,5,7,9])
    print(example)
    print(runningSum("numslist", example))
    
