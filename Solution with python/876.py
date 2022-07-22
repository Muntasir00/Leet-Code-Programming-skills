def middleNode(head: ListNode):
    slow = fast = head 
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
    return slow

print(middleNode([1,2,3,4,5,6]))