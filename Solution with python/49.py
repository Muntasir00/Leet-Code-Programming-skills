from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        hashmap = defaultdict(list)
        for s in strs:
            # keys can be strings, bcz they are immutable.
            hashmap[str(sorted(s))].append(s)
        return hashmap.values()

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))