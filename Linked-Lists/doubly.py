class DLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    def __repr__(self) -> str:
        return "node data : {}".format(self.data)
    
    def get_data(self):
        """
        Return self.data attribute
        """
        return self.data
    
    def set_data(self, new_data):
        """
        Replace the existing value i.e self.data attribute with the new data
        """
        self.data = new_data

    def get_next(self):
        """
        Return self.next attribute to return the next node in our list
        """
        return self.next

    def set_next(self, new_next):
        """
        Replace the existing value of self.next attribute with the new_next data
        """
        self.next = new_next

    def get_prev(self):
        """
        Return self.prev attribute to return the previous node data
        """
        return self.prev

    def set_prev(self, prev_data):
        """
        Replace the existing value of self.prev with the prev_data
        """
        self.prev = prev_data

    