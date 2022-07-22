class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        p1 = 0
        p2 = 0
        n1 = len(word1)
        n2 = len(word2)
        
        while p1<n1 and p2<n2:
            ans += word1[p1] + word2[p2]
            p1+=1
            p2+=1
            
        if p1!=n1:
            ans+=word1[p1:]
        if p2!=n2:
            ans+= word2[p2:]
            
        return ans
        