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
    

    # remove_node is not working, figure out why before looking at code.
    def remove_node(self, value):
        current_node = self.head
        prev_node = None
        next_node = current_node.get_next_node()

        if prev_node == None and next_node == None:
            return 'Cannot remove only node in list.'
        while next_node:
            if current_node.get_value() == value:
                if prev_node == None:
                    self.head = next_node
                elif next_node == None:
                    prev_node.set_link_node(None)
                else:
                    prev_node.set_link_node(next_node)
                return f'Successfully removed {value}'
            prev_node = current_node
            current_node = current_node.get_next_node()
            next_node = current_node.get_next_node()

        
        return f'{value} was not found in the list'
    



# TESTING

db = Linked_List(0)
db.add_to_end(1)
db.add_to_beginning(2)
db.add_to_end(3)
db.add_to_beginning(4)
print(db.stringify_list())
print('')
db.remove_node(3)
db.remove_node(5)
print(db.stringify_list())