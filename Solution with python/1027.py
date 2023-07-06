class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [{} for i in range(n)]
        result = -1
        for j in range(1,n):
            for i in range(j):
                diff = nums[j]-nums[i]
                dp[j][diff]=1+dp[i].get(diff,0)
                result=max(result,dp[j][diff]+1)
                
        return result 
    
# s = Solution()
# print(s.longestArithSeqLength([9,4,7,2,10]))