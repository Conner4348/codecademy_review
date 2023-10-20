# Queue data structure
from nodes_and_linked_lists import Node

class Queue:

    def __init__(self, max_size=None):
        self.max_size = max_size
        self.head = None
        self.tail = None
        self.size = 0

    def Enqueue(self, val):
        node = Node(val)

        if self.tail == None:
            self.head = node
            self.tail = node
            self.size += 1
            return

        self.tail.set_link_node(node)
        self.tail = node
        self.size += 1

    def Dequeue(self):
        temp = self.head
        if self.size == 1:
            self.head = None
            self.tail = None
            return temp
        
        self.head = self.head.get_next_node()
        return temp
    
    def Peek(self):
        return self.head

# TESTING

#q = Queue()
#q.Enqueue(32)
#q.Enqueue(17)
#print(q.Peek().get_value())