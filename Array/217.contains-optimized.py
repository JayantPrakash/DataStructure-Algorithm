from typing import Optional, List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False     
    
sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))    
print(sol.containsDuplicate([1,2,3,4]))
                

        