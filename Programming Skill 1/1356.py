class solution:
    def sortByBits(self, arr:List[int])->List[int]:
        def bit_count(x):
            ans = []
            while x:
                ans.append(x%2)
                x=x//2
            return ans.count(1)
        
        arr.sort()
        return sorted(arr,key=lambda x: bit_count(x))