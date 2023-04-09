class DEQUEUE:
    def __init__(self):
        self.items = []

    def __repr__(self):
        return str(self.items)

    def add_front(self, item):
        self.items.insert(0, item)

    def peek_front(self):
        return self.items[0]

    def remove_front(self):
        self.items.pop(0)

    def add_rear(self, item):
        self.items.append(item)

    def peek_rear(self):
        return self.items[-1]

    def remove_rear(self):
        self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
