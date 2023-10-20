# Stack data structure
from nodes_and_linked_lists import Node

class Stack:

    def __init__(self, max_size=None):
        self.size = 0
        self.head = None
        self.max_size = max_size

    def Push(self, val):
        node = Node(val)
        if self.head != None:
            node.set_link_node(self.head)
        self.head = node
        self.size += 1

    def Pop(self):
        temp = self.head
        self.head = temp.get_next_node()
        self.size -= 1
        return temp
    
    def Peek(self):
        return self.head
    
    def stringify_list(self):
        string_list = ''

        current_node = self.head
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value())
                string_list += '\n'
                current_node = current_node.get_next_node()
        return string_list

# TESTING

#s = Stack()
#s.Push(12)
#s.Push(32)
#s.Push(47)
#s.Push(92)
#print(s.stringify_list())
#print(s.Peek().get_value())
#s.Pop()
#print(s.Peek().get_value())