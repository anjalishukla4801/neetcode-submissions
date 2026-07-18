class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        return [num for num,freqq in c.most_common(k)]

        