class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        ans = []

        for key, value in count.most_common()[:k]:
            ans.append(key)
        return ans