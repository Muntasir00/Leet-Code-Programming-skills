class Solution:
    def average(self, salary: List[int]) -> float:
        s=0
        for i in salary:
            s+=i   
        avg = (s-max(salary)-min(salary))/(len(salary)-2)
        return avg