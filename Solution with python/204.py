import math

class Solution:
    def countPrimes(self, n: int) -> int:  
        #initializing list containing n amount of 1's
        listofprimes = [1]*n
        
        #SIEVE OF ERATOSTHENES
        #starting at index 2, loop through until reaching sqrt of 
        i=2
        
        while i<= math.sqrt(n):
            #IF i is prime change all multiples of that number to 0
            if listofprimes[i]==1:
                j = i*2
                while j<n:
                    listofprimes[j]=0
                    j+=i
                    
            i+=1
            
        #remove first two indices (representing 0 and 1)
        del listofprimes[0:2]
        #return sum of list (remaining primes 0 and 1)
        return sum(listofprimes)
    
prime = Solution()
print(prime.countPrimes(10))