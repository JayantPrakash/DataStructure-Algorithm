from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_elems = set(nums)
        longest_seq = 0
        for num in nums:
            if num - 1 not in set_elems:
                curr_val = num
                length = 1
                while (curr_val + 1) in set_elems:
                    curr_val += 1
                    length += 1

                longest_seq = max(length, longest_seq)
        return longest_seq
        

sol = Solution()
nums = [100,4,200,1,3,2]
nums = [1,0,1,2]
nums = [0,3,7,2,5,8,4,6,0,1]
#nums = []
print(sol.longestConsecutive(nums))