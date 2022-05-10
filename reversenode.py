class Node:
    def __init__(self,data):
        self.data =data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def show(self):
        node=self.head
        while node is not None:
                str=" "
                for i in range(1,len(node.data)+1):
                    str+=node.data[-i]
                print(str)
                node=node.next
firstNode = Node("john")
linkedlist = Linkedlist()
linkedlist.printList()
    
firstNode = Node("john")
linkedlist = Linkedlist()

            