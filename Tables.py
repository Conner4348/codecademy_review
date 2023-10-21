# Table data structure

class HashMap:

    def __init__(self, size):
        self.size = size
        self.array = [None for i in range(size)]

    def Hash(self, key):
        data = key.encode()
        index = sum(data) % self.size
        return index
    
    def Assign(self, key, val):
        index = self.Hash(key)
        self.array[index] = [key, val]

    def PrintMap(self):
        for row in self.array:
            print(row)

    def collision(self, index):
        index += 1
        if self.array[index] != None:
            pass
        # Work on collisions
    
# TESTING

hm = HashMap(5)
hm.Assign('7', 'Well that was fun')
hm.PrintMap()