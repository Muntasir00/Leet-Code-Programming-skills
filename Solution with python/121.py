class Solution:
    def max_profit(self,prices):
        n = len(prices)
        left, right = 0,1
        max_profit = 0
        while right<n:
            current_profit = prices[right]-prices[left]
            if prices[left]<prices[right]:
                max_profit = max(current_profit,max_profit)
            else:
                left = right
            right += 1
a = Solution()
a.max_profit([7,1,5,3,6,4])