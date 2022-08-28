class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p=1
        s=0
        while n>0:
            x = n%10
            p*=x
            s+=x
            n=n//10
        return p-s 