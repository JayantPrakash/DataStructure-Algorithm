from typing import Optional, List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        dict = {}

        for i, elem in enumerate(nums):
            if elem not in dict.keys():
                dict[elem] = i
            else:
                return True

        return False    
    
sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))    
print(sol.containsDuplicate([1,2,3,4]))
                

        