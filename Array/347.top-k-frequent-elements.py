from typing import Optional, List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_elem = {}

        for i in range(len(nums)):
            if nums[i] in dict_elem:
                dict_elem[nums[i]] = dict_elem[nums[i]] + 1
            else:
                dict_elem[nums[i]] = 1


        dict_elem = dict(sorted(dict_elem.items(),
                                key = lambda item : item[1], reverse = True))

        keys = list(dict_elem.keys())
        return keys[0:k]    


sol = Solution()

print(sol.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
print(sol.topKFrequent( nums = [1], k = 1))
print(sol.topKFrequent(nums = [1,2,1,2,1,2,3,1,3,2], k = 2))