from collections import defaultdict
class Solution:
    def maxVowels(self,s, k):
        VOWELS = defaultdict(int)
        VOWELS['a']=VOWELS['e']=VOWELS['i']=VOWELS['o']=VOWELS['u']=1
        s = [VOWELS[c] for c in s]
        print(s)
        print(type(s))
        max_count = count = sum(s[:k])
        for i in range(len(s)-k):
            count += s[i+k]-s[i]
            if count > max_count:
                max_count = count
        return max_count
    
a = Solution()
print(a.maxVowels("abciiidef",3))