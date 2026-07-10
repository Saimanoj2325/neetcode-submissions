from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mpp = defaultdict(int)
        left = 0
        maxi = 0
        for right in range(len(s)):
            mpp[s[right]] += 1
            while mpp[s[right]] > 1:
                mpp[s[left]] -= 1
                if mpp[s[left]] == 0:
                    del mpp[s[left]]
                left += 1
            maxi = max(maxi,right-left+1)
        return maxi