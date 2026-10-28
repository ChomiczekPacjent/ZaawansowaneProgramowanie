from models.book import Book
from models.employee import Employee
from models.library import Library
from models.order import Order
from models.student import Student


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
