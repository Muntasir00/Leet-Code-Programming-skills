class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i =="{" or i=="[":
                stack.append(i)
            elif(len(stack)):
                el = stack.pop()
                if el == "(" and i == ")":
                    continue
                if el == "{" and i == "}":
                    continue
                if el == "[" and i == "]":
                    continue
                else:
                    return False
            else:
                return False
        if(len(stack)):
            return False
        else:
            return True
s =Solution()
print(s.isValid("(]"))
            