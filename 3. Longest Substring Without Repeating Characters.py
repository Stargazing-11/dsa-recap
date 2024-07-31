from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        count_letters = defaultdict(int)
        max_length = 1

        left = 0

        for right in range(len(s)):
            count_letters[s[right]] += 1

            while left < right and count_letters[s[right]] > 1:
                max_length = max(max_length, right - left)
                count_letters[s[left]] -= 1
                left += 1
        
            max_length = max(max_length, right + 1 - left)
        return max_length