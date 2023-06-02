class SLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self) -> str:
        return "node data : {}".format(self.data)
    
    def get_data(self):
        """Return self.data attribute"""
        return self.data
    
    def set_data(self, new_data):
        """Replace the existing value i.e self.data attribute with the new data"""
        self.data = new_data

    def get_next(self):
        """Return self.next attribute to return the next node in our list"""
        return self.next

    def set_next(self, new_next):
        """Replace the existing value of self.next attribute with the new_next data"""
        self.next = new_next

    


class SLL:
    
    def __init__(self):
        self.head = None

    def __repr__(self):
        return "SLL object head = {}:".format(self.head)
    
    def is_empty(self):
        """Return True if the linked list is empty else False if not"""
        return self.head is None
    
    def add_front(self, new_data):
        temp = SLLNode(new_data)
        temp.set_next(self.head)
        self.head = temp


    # finding the size of our linked list
    def size(self):
        """
            This function traverses the linked list and return the size or the number of nodes present
        
            Time complexity is O(n) :- since we are traversing/visiting through all the nodes to get the exact size/number of nodes present
        """
        size = 0

        if self.head is None:
            return size
        
        temp = self.head

        while temp is not None:
            size += 1
            temp = temp.get_next()
        return size
    

    # searching for a node data in our linked list
    def search(self, data):
        """
            Traverse the list and return True if data is present else return False
            Time complexity = O(N)
        """
        if self.head is None:
            return "Linked list is empty hence no nodes to search through"
        
        temp = self.head

        while temp is not None:
            if temp.get_data() == data:
                return True
            temp = temp.get_next()
        return False


    # remove a node data
    def remove(self, data):
        """
            Remove 1st occurence of a node that contains the data to be removed as it's self.data variable and return nothing
        """
        if self.head is None:
            return "The linked list is empty hence no nodes to remove"
        
        curr = self.head
        previous = None
        found = False

        while not found:
            if curr.get_data() == data:
                found = True
            else:
                if curr.get_next() == None:
                    return "No node with that value is found"
                else:
                    previous = curr
                    curr = curr.get_next()
        if previous is None:
            self.head = curr.get_next()
        else:
            previous.set_next(curr.get_next)


    # reversing our linked lists
    def reverse(self, head):
        prev, curr = None, head

        while curr:
            node = curr.next
            curr.next = prev
            prev = curr
            curr = node
        return prev
    

    # checking if there's a cycle in our linked list
    def cycle(self):
        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                pass
    
       

        
        
    