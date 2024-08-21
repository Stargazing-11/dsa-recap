class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}

        def dp(n): 
            if n >= len(nums) -1: 
                return 0
            if n not in memo: 
                min_jump = float("inf")
                for i in range(1, nums[n] + 1):
                    min_jump = min(min_jump, dp(n + i) + 1)
                memo[n] = min_jump
            return memo[n]
        
        return dp(0)
