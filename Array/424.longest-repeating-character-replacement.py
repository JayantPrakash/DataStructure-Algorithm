class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        max_len = 0
        count = {}
        for R in range(len(s)):
            count[s[R]] = count.get(s[R],0) + 1

            while (R-L + 1) - max(count.values()) > k:
                count[s[L]] -= 1
                L += 1

            max_len = max(R-L+1, max_len)    
        return max_len

sol = Solution()
s = "ABAB"
k = 2
print(sol.characterReplacement(s,k))       


"""
T(n) = O(nm)
S(n) = O(m)
"""