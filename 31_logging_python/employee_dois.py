import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

FORMAT = '%(asctime)s:%(levelname)s:%(module)s:%(filename)s:%(message)s'
formatter = logging.Formatter(FORMAT)

file_handler = logging.FileHandler('log/employee_dois.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class Employee:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        logger.info(f'Created Employee: {self.first_name} - {self.last_name}')

    @property
    def email(self):
        return f'{self.first_name}.{self.last_name}@email.com'

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

emp_1 = Employee('Walter', 'White')
emp_2 = Employee('Jesse', 'Pinkman')

