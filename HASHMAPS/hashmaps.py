class Hashmap:
    def __init__(self):
        self.hashmap = {}

    
    def __repr__(self):
        return str(self.hashmap)

    def dicts(self, strs):
        for item in strs:
            self.hashmap[item] = self.hashmap.get(item, 0) + 1
        return self.hashmap