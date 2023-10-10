# Nodes and Linked Lists

class Node:

    def __init__(self, value, link=None):
        self.value = value
        self.link = link

    def set_link_node(self, link):
        self.link = link

    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.link
    




class Linked_List:

    def __init__(self, value):
        self.head = Node(value)

    def add_to_end(self, value):
        node_to_add = Node(value)

        current_node = self.head
        while current_node.get_next_node():
            current_node = current_node.get_next_node()
        current_node.set_link_node(node_to_add)

    def add_to_beginning(self, value):
        node_to_add = Node(value)

        node_to_add.set_link_node(self.head)
        self.head = node_to_add

    def stringify_list(self):
        string_list = ''

        current_node = self.head
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value())
                string_list += '\n'
                current_node = current_node.get_next_node()
        return string_list
    
    def get_head_node(self):
        return self.head
    
    def remove_node(self, value):

        current_node = self.get_head_node()
        next_node = 'temp'
        
        if current_node.get_value() == value:
            if current_node.get_next_node() == None:
                self.head = None
            else:
                self.head = current_node.get_next_node()
        else:
            while next_node:
                print(f'The value of the current node is {current_node.get_value()}')
                next_node = current_node.get_next_node()
                if  next_node == None:
                    continue # continue moves onto the next iteration which will break the loop, since next_node is None.
                if next_node.get_value() == value:
                    if next_node != None: # Making sure next_node is not None prevents error.
                        current_node.set_link_node(next_node.get_next_node())
                    else:
                        current_node.set_link_node(None)
                    next_node = None
                else:
                    current_node = next_node

    def swap_nodes(self, value_one, value_two):
        pass
    



# TESTING

db = Linked_List(0)
db.add_to_end(1)
db.add_to_beginning(2)
db.add_to_end(3)
db.add_to_beginning(4)
print(db.stringify_list())
print('')
#db.remove_node(3)
#db.remove_node(5)
#db.remove_node(2)
db.remove_node(4)
print(db.stringify_list())
