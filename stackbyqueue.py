class Stacks():
    def __init__(self):
        self.q1=[]
        self.q2=[]
    def push(self,x):
        if len(self.q1)==0:
            self.q1.append(x)
            print("added")
        else:
            for i in range(len(self.q1)):
                self.q2.append(self.q1.pop(0))
            self.q1.append(x)
            for j in range(len(self.q2)):
                self.q1.append(self.q2.pop(0))

    def pop(self):
            return self.q1.pop(0)

s1=Stacks()
s1.push(1)
s1.push(2)
s1.push(3)
print(s1.pop())
print(s1.pop())
print(s1.pop())

class Stack:
def __init__(self):
    self.queue1 = Queue()
    self.queue2 = Queue()

def is_empty(self):
    return self.queue2.is_empty()

def push(self, data):
    self.queue1.enqueue(data)
    while not self.queue2.is_empty():
        x = self.queue2.dequeue()
        self.queue1.enqueue(x)
    self.queue1, self.queue2 = self.queue2, self.queue1

def pop(self):
    return self.queue2.dequeue()
 
class Queue:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def enqueue(self, data):
        self.items.append(data)
 
    def dequeue(self):
        return self.items.pop(0)
 
 
s = Stack()
 
print('Menu')
print('push <value>')
print('pop')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'push':
        s.push(int(do[1]))
    elif operation == 'pop':
        if s.is_empty():
            print('Stack is empty.')
        else:
            print('Popped value: ', s.pop())
    elif operation == 'quit':
        break
