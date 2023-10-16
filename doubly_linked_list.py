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
    

# TESTING

db = Doubly_Linked_List(3)
print(db.check_size())
print(db.get_head_node())
print(db.get_tail_node())