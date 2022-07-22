class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=0
        c=0
        for i in s:
            if i==" ":
                c=0
            else:
                c+=1
                a=c
        return a