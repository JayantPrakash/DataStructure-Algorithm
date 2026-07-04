from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            length = min(height[l], height[r])
            breadth = r - l
            local_area = length * breadth
            max_area =  max(max_area, local_area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1     

        return max_area

sol = Solution()
height = [1,8,6,2,5,4,8,3,7]
height = [1,1]
print(sol.maxArea(height))
