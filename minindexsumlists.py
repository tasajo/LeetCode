'''
599. Minimum Index Sum of Two Lists
Suppose Andy and Doris want to choose a restaurant for dinner, and they 
both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least 
list index sum. If there is a choice tie between answers, output all of 
them with no order requirement.
'''
from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        fav = {r:i for i,r in enumerate(list1)}
        res = []
        min_ix = float('inf')
        
        for i, r in enumerate(list2):
            if r in fav:
                if i + fav[r] == min_ix:
                    res.append(r)
                elif i + fav[r] < min_ix:
                    res = [r]
                    min_ix = i + fav[r]
                    
        return res

s = Solution()
print(s.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],
["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))
'''
Explanation: The only restaurant they both like is "Shogun".
'''

print(s.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],
["KFC","Shogun","Burger King"]))
'''
Explanation: The restaurant they both like and have the least index sum 
is "Shogun" with index sum 1 (0+1).
'''

print(s.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], 
["KFC","Burger King","Tapioca Express","Shogun"]))

print(s.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], 
["KNN","KFC","Burger King","Tapioca Express","Shogun"]))

print(s.findRestaurant(["KFC"], ["KFC"]))
