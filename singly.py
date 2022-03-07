class Node:
    def __init__(self,data):
        self.data =data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def islistEmpty(self):
        if self.head is None:
            return True
        else:
            return False
    def listLength(self):
        currentNode = self.head
        length =0
        while currentNode is not None:
            length+=1
            currentNode = currentNode.next
        return length
    def insertHead(self,newNode):
        temporaryNode = self.head
        self.head = newNode
        self.head.next = temporaryNode
        del temporaryNode
    def insertAt(self,newNode,position):
        if position < 0 or position > self.listLength():
            print("Invalid  position")
            return 
        if position == 0:
            self.insertHead(newNode)
            return
        currentNode = self.head
        currentePosition = 0
        while True:
            if currentePosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentePosition +=1
    def insertEnd(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next  is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
    def deleteHead(self):
        if self.islistEmpty() is False:
            previousHead =self.head
            self.head = self.head.next
            previousHead.next = None
        else:
            print("linked list is empty,delete failed")
    def deleteAt(self,position):
        if position < 0 or position >= self.listLength():
            print("Invalid position")
            return 
        if self.islistEmpty() is False:
            if position == 0:
                self.deleteHead()
                return
                
        currentNode = self.head
        currentPosition = 0 
        while True:
            if currentPosition == position:
                previousNode.next = currentNode.next
                currentNode.next = None
                break
                
            previousNode = currentNode
            currentNode = currentNode.next
            
            currentPosition+=1
                
            
        
        
    def deleteEnd(self):
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        previousNode.next = None
    def detectCycle(self):
        fast =self.head
        slow =self.head
        loopexist =0
        while(fast!=None and slow!=None and fast.next !=None):
            fast = fast.next.next
            slow = slow.next
            if (fast==slow):
                loopexist=1
                break
        if (loopexist):
            print("loop exist")
            slow =self.head
            while (slow!=fast):
                slow =slow.next
                fast =fast.next
            return slow
        print("loop doesnot exist")
        return  None
    def printList(self):
        if self.head is None:
            print("List is empty")
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next
firstNode = Node("john")
linkedlist = Linkedlist()
linkedlist.insertEnd(firstNode)
secondNode = Node("ben")
linkedlist.insertEnd(secondNode)
thirdNode = Node("mathew")
linkedlist.insertEnd(thirdNode)
linkedlist.insertEnd(secondNode)
linkedlist.detectCycle()
# linkedlist.deleteAt(1)
# linkedlist.printList()


