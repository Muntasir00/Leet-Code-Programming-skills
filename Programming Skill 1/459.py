class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
    """
        def getFactorsExlusive(number):
            factors=[]
            for i in range(1, number): #Exlusive at the end
                if number % i == 0:
                    factors.append(i)
            return factors        
        
        factors=getFactorsExlusive(len(s))
       
        subs=set()
        for f in factors: 
            subs.add(s[0:f])
        
        for substr in subs:
            if (s == (int)(len(s)/len(substr))*substr):
                return True 