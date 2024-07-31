import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canEatAll(k):
            cur_hours = 0

            for pile in piles:
                cur_hours += math.ceil(pile / k)
            return cur_hours <= h

        low, high = 1, max(piles)

        while low < high:
            mid = (low + high) // 2

            if canEatAll(mid):
                high = mid
            else:
                low = mid + 1
        return low