class AllList():
    
    def __init__(self, items):
        self.items = items
        
    def get_Node(self, id):
        return self.items[id]
    
    def get_nodes(self):
        return list(self.items.values())
    
    def get_all(self):
        return self.items.items()