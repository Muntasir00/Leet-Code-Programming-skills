class NumArray:
    
    def __init__(self, nums: List[int]):
        self.nums=nums
        s=0
        self.lst=[]
        for i in nums:
            s+=i
            self.lst.append(s)
            
        

    def sumRange(self, left: int, right: int) -> int:
        #return sum(self.nums[left:right+1])
        if left>0 and right>0:
            return self.lst[right]-self.lst[left-1]
        else:
            return self.lst[right]