class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ""
        if digits[len(digits)-1] == 9:
            for x in digits:
                s +=str(x)
            s = str(int(s)+1)
            digits = []
            for x in s:
                digits.append(int(x))
        else:
             digits[len(digits)-1]+=1
        return  digits