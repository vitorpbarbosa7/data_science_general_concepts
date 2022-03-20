# Replace print statements with log statements

import logging

## DEBUG: Detailed information, typically of interest only when diagnosing problems

## INFO: Confirmation that things are working as expected

## WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. 'disk space low'). The software is still working as expected.
### (DEFAULT LEVEL)

## ERROR: Due to a more serious problem, the software has not been able to perform some function

## CRITICAL: A serious error, indicating that the program itself may be unable to continue running

logging.basicConfig(filename = 'test.log',
                    level = logging.DEBUG, 
                    format = '%(asctime)s:%(filename)s:%(levelname)s:%(message)s')

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
    return x / y

# if __name__ == '__main__':
NUM_1 = 20
NUM_2 = 10

add_result = add(NUM_1, NUM_2)
subtract_result = subtract(NUM_1, NUM_2)
multiply_result = multiply(NUM_1, NUM_2)
divide_result = divide(NUM_1, NUM_2)

logging.debug(f'Add {NUM_1} + {NUM_2} = {add_result}')
logging.debug(f'Subtract {NUM_1} - {NUM_2} = {subtract_result}')
logging.debug(f'Multiply {NUM_1} * {NUM_2} = {multiply_result}')
logging.debug(f'Divide {NUM_1} / {NUM_2} = {divide_result}')




