import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

FORMAT = '%(asctime)s:%(levelname)s:%(module)s:%(filename)s:%(message)s'
formatter = logging.Formatter(FORMAT)

file_handler = logging.FileHandler('log/assert.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def divide(x, y):
    try:
        assert y != 0
    except Exception as e:
        logger.exception(f'Can not divide by zero - {e}')
    else:
        return x / y

if __name__ == '__main__':
    X = 4
    Y = 0
    print(divide(X,Y))