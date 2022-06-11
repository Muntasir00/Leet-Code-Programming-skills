class Solution(object):
    def getDecimalValue(self,head):
        res = []
        while head:
            res.append(str(head.val))
            head=head.next 
        x=''.join(res)
        return int(x,2)