class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x==0):
            return True
        if(x<0):
            return False
        num,pr = x,0
        while(x>0):
            temp = x%10
            pr = pr*10+temp
            x = x//10
        if(num==pr):
            return True
        return False

s = Solution()
print(s.isPalindrome(121))