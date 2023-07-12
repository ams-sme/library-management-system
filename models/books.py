class Book():
    
    def __init__(self, name, author, quantity):
        self.name = name
        self.author = author
        self.quantity = quantity
        
    def get_count(self):
        return 0
    
    def something(self):
        print("something")
        return 1