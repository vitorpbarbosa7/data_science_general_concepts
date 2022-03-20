import logging

format_logging = '%(asctime)s:%(module)s:%(filename)s:%(levelname)s:%(message)s'
logging.basicConfig(filename='employee.log', 
                    level=logging.INFO, 
                    format=format_logging)

class Employee:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        logging.info(f'Created Employee: {self.first_name} - {self.last_name}')

    @property
    def email(self):
        return f'{self.first_name}.{self.last_name}@email.com'

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

emp_1 = Employee('Walter', 'White')
emp_2 = Employee('Jesse', 'Pinkman')

