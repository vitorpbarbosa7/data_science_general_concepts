import logging
import employee_dois

# Return the module of your application
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('logging_explore.log')

# Exploring options
FORMAT = '''%(asctime)s:\
%(funcName)s:\
%(module)s:\
%(filename)s:\
%(levelname)s:\
%(levelno)s:\
%(lineno)d:\
%(message)s:\
%(process)d:\
%(relativeCreated)d:\
%(msecs)d
'''

formatter = logging.Formatter(FORMAT) 
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
