class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return str(self.data)
    
    def search(self, target):
        if self.data == target:
            return f"Node item found: {self.data}"
        
        if self.left and  self.data > target:
            return self.left.search(target)
        
        if self.right and self.data < target:
            return self.right.search(target)
        
        return "No Node found matching your target"


    