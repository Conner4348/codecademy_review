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

    def remove_head(self):
        new_head = self.head.get_next_node()
        new_head.set_prev_node(None)
        self.head = new_head

    def remove_tail(self):
        new_tail = self.tail.get_prev_node()
        new_tail.set_next_node(None)
        self.tail = new_tail

    def stringify_list(self):
        string_list = ''

        current_node = self.head
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value())
                string_list += '\n'
                current_node = current_node.get_next_node()
        return string_list
    
    def remove_node(self, value):
        current_node = self.head

        if current_node.get_value() == value:
            self.remove_head()
            return
        
        current_node = current_node.get_next_node()
        while True:
            if current_node.get_value() == value:
                prev_node = current_node.get_prev_node()
                next_node = current_node.get_next_node()
                break
            current_node = current_node.get_next_node()
            if current_node == None:
                print('Could not find value in list.')
                return
            
        if next_node == None:
            self.remove_tail()
        else:
            next_node.set_prev_node(prev_node)
            prev_node.set_next_node(next_node)
        
    

# TESTING

db = Doubly_Linked_List(3)
db.add_to_end(1)
db.add_to_beginning(2)
db.add_to_beginning(4)
db.add_to_beginning(7)
db.add_to_beginning(9)
db.add_to_beginning(0)
db.add_to_beginning(5)
db.add_to_beginning(6)
db.add_to_beginning(8)
print(db.stringify_list())
print('')
db.remove_node(2)
print(db.stringify_list())