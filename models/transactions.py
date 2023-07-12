class Transactions():
    
    def __init__(self, book, borrower, tenure, return_date):
        self.book = book
        self.borrower = borrower
        self.tenure = tenure
        self.return_date = return_date
        
    def borrow(self):
        return self.book 