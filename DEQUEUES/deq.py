class DEQUEUE:
    def __init__(self):
        self.items = []

    def __repr__(self):
        return str(self.items)

    def add_front(self, item):
        self.items.insert(0, item)

    def peek_front(self):
        return self.items[0] if self.items else []

    def remove_front(self):
        return self.items.pop(0) if self.items else []

    def add_rear(self, item):
        self.items.append(item)

    def peek_rear(self):
        return self.items[-1] if self.items else []

    def remove_rear(self):
        return self.items.pop() if self.items else []
    
    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
