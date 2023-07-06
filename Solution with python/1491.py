class Solution:
    def average(self, salary: List[int]) -> float:
        c = []
        a = max(salary)
        b = min(salary)
        for i in range(len(salary)):
            if salary[i]!=a and salary[i]!=b:
                c.append(salary[i])
        return sum(c)/len(c)