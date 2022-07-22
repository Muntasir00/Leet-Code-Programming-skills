class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return sorted(s)==sorted(t)
        #return Counter(s)==Counter(t)
        counts,countt={},{}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            counts[s[i]]=1+counts.get(s[i],0)
            countt[t[i]]=1+countt.get(t[i],0)
        for c in counts:
            if counts[c] != countt.get(c,0):
                return False
        print(counts,countt)
        return True
            