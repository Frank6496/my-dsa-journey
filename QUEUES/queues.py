class Queue:
    def __init__(self):
        self.q = []

    def __repr__(self):
        return str(self.q)

    def enqueue(self, data):
        """Adds the item at the back of our queue [FIFO :- Principle]"""
        self.q.insert(0, data)

    def dequeue(self):
        """Removes the 1st(front) item in our queue [FIFO :- Principle]"""
        return self.q.pop() if self.q else None
    
    def size(self):
        """Returns the size or the count of item in our queue"""
        return len(self.q)
    
    def is_empty(self):
        """Returns True if the queue is empty else return False"""
        return  not self.q

