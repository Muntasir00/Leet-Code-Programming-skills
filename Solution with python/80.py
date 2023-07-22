# #Easy Approach
# class Solution:
#     def removeDuplicates(self, nums):
#         for i in range(len(nums)-2,0,-1):
#             if (nums[i]==nums[i-1]) and (nums[i]==nums[i+1]):
#                 nums.pop(i+1)
#         return len(nums)
# a = Solution()
# a.removeDuplicates([0,0,1,1,1,1,2,3,3])

#Two Pointer Approach
class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        l,r=0,1
        c = True
        while r<n:
            if nums[l] == nums[r]:
                if c:
                    c = False
                    l += 1
                    nums[l] = nums[r]
            elif nums[l]!=nums[r]:
                l +=1
                nums[l]=nums[r]
                c=True
            r+=1
        return l+1
    
a = Solution()
print(a.removeDuplicates([0,0,1,1,1,1,2,3,3]))
    
                    
