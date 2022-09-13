class Solution:
    def oppositeTask(n):
        return 0,n 

def main():
    cases = int(input())
    for caseno in range(1,cases+1):
        n = map(int, input().split())
        result = Solution.oppositeTask(n)
        print(f"Case {caseno}: {result}")

main()