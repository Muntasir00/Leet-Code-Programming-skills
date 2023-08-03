class Solution:
    def rotate(self,nums,k):
        n=len(nums)
        k = k%n 
        nums[:n-k]= nums[:n-k][::-1]
        nums[n-k:]=nums[n-k:][::-1]
        nums[:]=nums[::-1]
        return nums
    
    
a = Solution()
print(a.rotate([1,2,3,4,5,6,7],3))