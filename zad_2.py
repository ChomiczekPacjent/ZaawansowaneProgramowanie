class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (f'Biblioteka: {self.city}, ul. {self.street}, '
                f'{self.zip_code}, godziny: {self.open_hours}, '
                f'tel. {self.phone}')


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date,
                 city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f'Pracownik {self.first_name} {self.last_name} '
                f'({self.city}, ul. {self.street}, {self.zip_code}), '
                f'zatrudniony {self.hire_date}, ur. {self.birth_date}, '
                f'tel. {self.phone}')


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'Student {self.first_name} {self.last_name}'


class Book:
    def __init__(self, library, publication_date, author_name,
                 author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f'Książka: {self.author_name} {self.author_surname}, '
                f'wyd. {self.publication_date}, '
                f'{self.number_of_pages} stron | {self.library}')


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


library_1 = Library('Katowice', 'Mazowiecka', '43-350', '8-14',
                    '111222333')
library_2 = Library('Katowice', 'Winowoska', '43-349', '8-15',
                    '112223334')

book_1 = Book(library_1, '22.01.2010', 'Maryla', 'Rodowska', 700)
book_2 = Book(library_2, '21.01.2010', 'Joryla', 'Jorylos', 500)
book_3 = Book(library_1, '20.01.2010', 'Wiesława', 'Wiosławska', 400)
book_4 = Book(library_2, '23.01.2010', 'Marynada', 'Marynodowska', 300)
book_5 = Book(library_1, '24.01.2010', 'Jolanta', 'Jolowska', 777)

employee_1 = Employee('Dan', 'Nad', '20.10.2025', '20.05.2000',
                      'Wrocław', 'Wojta', '30-700', '878757727')
employee_2 = Employee('Pan', 'Nap', '10.10.2025', '07.05.2000',
                      'Katowice', 'Kojta', '45-700', '778757727')
employee_3 = Employee('Jan', 'Naj', '01.09.2024', '15.03.1998',
                      'Bytom', 'Długa', '41-900', '600700800')

student_1 = Student('Darek', 'Darkowski')
student_2 = Student('Jarek', 'Jarkowski')
student_3 = Student('Marek', 'Markowski')

order_1 = Order(employee_1, student_1, [book_1, book_3], '10.10.2026')
order_2 = Order(employee_2, student_2, [book_2, book_4, book_5],
                '12.10.2026')

print(order_1)
print()
print(order_2)
