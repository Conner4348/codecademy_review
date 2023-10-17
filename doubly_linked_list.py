# Doubly linked list

class Node_D:

    def __init__(self, value, next_link=None, prev_link=None):
        self.value = value
        self.next_link = next_link
        self.prev_link = prev_link

    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_link
    
    def get_prev_node(self):
        return self.prev_link
    
    def set_next_node(self, node):
        self.next_link = node
    
    def set_prev_node(self, node):
        self.prev_link = node
    


class Doubly_Linked_List:

    def __init__(self, value, max_size=None):
        self.head = Node_D(value)
        self.tail = None

    def get_head_node(self):
        return self.head
    
    def get_tail_node(self):
        return self.tail
    
    def check_size(self):
        counter = 0
        current_node = self.head

        while current_node:
            counter += 1
            current_node = current_node.get_next_node()
        return counter
    
    def add_to_beginning(self, value):
        node_to_add = Node_D(value)
        node_to_add.set_next_node(self.head)
        self.head.set_prev_node(node_to_add)
        self.head = node_to_add

    def add_to_end(self, value):
        node_to_add = Node_D(value)
        
        if self.get_tail_node() == None:
            current_node = self.head
            while current_node:
                if current_node.get_next_node() == None:
                    self.tail = current_node
                    current_node = None
                else:
                    current_node = current_node.get_next_node()

        node_to_add.set_prev_node(self.tail)
        self.tail.set_next_node(node_to_add)
        self.tail = node_to_add

        
    

# TESTING

db = Doubly_Linked_List(3)
print(db.check_size())
print(db.get_head_node().get_value())
print(db.get_tail_node())
db.add_to_beginning(8)
db.add_to_end(3)
db.add_to_end(4)
db.add_to_beginning(7)
print(db.check_size())
print(db.get_head_node().get_value())
print(db.get_tail_node().get_value())