class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        
        def calculate_water(left, right):
            return min(height[left], height[right]) * (right - left)

        most_water = calculate_water(left, right)

        while left < right:
            most_water = max(most_water, calculate_water(left, right))

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return most_water