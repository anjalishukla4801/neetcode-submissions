class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        max_len=0
        for i in nums:
            if i-1 not in s:
                current=i
                count=1
                while current+1 in s:
                    current+=1
                    count+=1
                max_len=max(max_len,count)
        return max_len