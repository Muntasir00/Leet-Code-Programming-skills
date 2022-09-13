#create nodes
#create linked list
#Add nodes to linked list
#print linked list

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def insertHead(self,newNode):
        temporaryNode = self.head
        self.head = newNode
        self.head.next = temporaryNode
        del temporaryNode

    def insertat(self, newNode, position):
        currentNode = self.head 
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break 
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition+=1


    def insert(self,newNode):
        if self.head is None:
            self.head = newNode 
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break 
                lastNode = lastNode.next 
            lastNode.next = newNode 
    def printlist(self):
        currentNode = self.head
        while True: 
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next
    

#Node => data ,next
firstNode = Node("John")
linkedList = LinkedList()
linkedList.insert(firstNode)
secondNode = Node("Ben")
linkedList.insert(secondNode)
thirdNode = Node("Mathew")
linkedList.insert(thirdNode)
fourthNode = Node("Don")
linkedList.insertHead(fourthNode)
fifthNode = Node("Rakib")
linkedList.insertat(fifthNode,1)
linkedList.printlist()
