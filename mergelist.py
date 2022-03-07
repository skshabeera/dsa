from singly import Node,Linkedlist

def mergeLists(firstList,secondList,mergedList):
    currentFirst = firstList.head
    currentSecond = secondList.head
    while True:
        if currentFirst is None:
            mergedList.insertEnd(currentSecond)
            break
        if currentSecond is None:
            mergedList.insertEnd(currentFirst)
            break
        if currentFirst.data< currentSecond.data:
            currentFirstNext = currentFirst.next
            currentFirst.next =None
            mergedList.insertEnd(currentFirst)
            currentFirst = currentFirstNext
        else:
            currentSecondNext = currentSecond.next
            currentSecond.next = None
            mergedList.insertEnd(currentSecond)
            currentSecond = currentSecondNext
            



nodeOne =Node(1)
nodeTwo =Node(3)
nodeThree =Node(4)
firstList = Linkedlist()
firstList.insertEnd(nodeOne)
firstList.insertEnd(nodeTwo)
firstList.insertEnd(nodeThree)

nodeFour =Node(2)
nodeFive =Node(7)
nodeSix =Node(9)
secondList =Linkedlist()
secondList.insertEnd(nodeFour)
secondList.insertEnd(nodeFive)
secondList.insertEnd(nodeSix)

print("printitng first List")
firstList.printList()
print("printing second List")
secondList.printList()

mergedList = Linkedlist()
mergeLists(firstList,secondList,mergedList)
# del firstList
# del secondList

print("printing Merged List")
mergedList.printList()




