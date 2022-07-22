class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        N = len(arr)
        total = 0
        for k in range(1,N+1,2):
            for t in range(N-k+1):
                total += sum(arr[t:t+k])
        return total
        