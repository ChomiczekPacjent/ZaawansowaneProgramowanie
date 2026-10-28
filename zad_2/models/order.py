class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = '\n'.join(f'  - {book}' for book in self.books)
        return (f'Zamówienie z dnia {self.order_date}\n'
                f'{self.student}\n'
                f'Obsługuje: {self.employee}\n'
                f'Książki:\n{books_str}')
