class Solution:
    def maxOperations(self, nums, k):
        l,r = 0,len(nums)-1
        nums.sort()
        count = 0
        while l<r:
            if nums[l]+nums[r]==k:
                count +=1
                l+=1
                r-=1
            elif nums[l]+nums[r]>k:
                r-=1
            else:
                l+=1
                
        return count
    
a = Solution()
a.maxOperations([1,2,3,4],5)