class Solution:
    def climbStairs(self, n: int) -> int:
        if n<3:
            return n
        prev=1
        prev2=2
        for i in range(3,n+1):
            prev,prev2=prev2,prev+prev2
        return prev2

        