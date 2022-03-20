import logging
import employee_dois

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

FORMAT = '%(asctime)s:%(levelname)s:%(module)s:%(filename)s:%(message)s'
formatter = logging.Formatter(FORMAT)

file_handler = logging.FileHandler('log/sample.log')
logger.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

# stream handler makes it possible to show it in the console
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

## DEBUG: Detailed information, typically of interest only when diagnosing problems

## INFO: Confirmation that things are working as expected

## WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. 'disk space low'). The software is still working as expected.
### (DEFAULT LEVEL)

## ERROR: Due to a more serious problem, the software has not been able to perform some function

## CRITICAL: A serious error, indicating that the program itself may be unable to continue running

format_logging = '%(asctime)s:%(levelname)s:%(module)s:%(filename)s:%(message)s'
logging.basicConfig(filename='sample.log', 
                    level=logging.INFO, 
                    format=format_logging)


def add(x, y):
    '''
    Adds two nunbers
    '''
    return x + y

def subtract(x, y):
    '''
    Subtracts two numbers
    '''
    return x - y 

def multiply(x, y):
    '''
    Multiplies two numbers
    '''
    return x * y

def divide(x, y):
    '''
    Divides two numbers
    '''
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception('Tried to divide by zero')
    else: 
        return result

# if __name__ == '__main__':
NUM_1 = 20
NUM_2 = 0

add_result = add(NUM_1, NUM_2)
subtract_result = subtract(NUM_1, NUM_2)
multiply_result = multiply(NUM_1, NUM_2)
divide_result = divide(NUM_1, NUM_2)

logger.debug(f'Add {NUM_1} + {NUM_2} = {add_result}')
logger.debug(f'Subtract {NUM_1} - {NUM_2} = {subtract_result}')
logger.debug(f'Multiply {NUM_1} * {NUM_2} = {multiply_result}')
logger.debug(f'Divide {NUM_1} / {NUM_2} = {divide_result}')




