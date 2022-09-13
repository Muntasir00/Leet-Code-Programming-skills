import math
N = 1000010
def main():
    sum1 = [0]*1000001
    sum1[0]=0
    for i in range(1,1000001):
        sum1[i]=sum1[i-1]+math.log(i);
    cases = int(input())
    for caseno in range(1, cases + 1):
        n, m = map(int, input().split())
        result = int(sum1[n]/(math.log(m)) +1)
        print(f"Case {caseno}: {result}")
main()