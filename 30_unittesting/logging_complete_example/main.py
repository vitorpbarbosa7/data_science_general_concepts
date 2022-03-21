import datetime
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

FORMAT = '%(asctime)s:%(levelname)s:%(module)s:%(filename)s:%(message)s'
formatter = logging.Formatter(FORMAT)

file_handler = logging.FileHandler('log/trycatch_example.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class Book:
    author: str
    page_count: int
    publication_date: datetime.date
    title: str

    def __eq__(self, other):
        """Determines if passed object is equivalent to current object."""
        return self.__dict__ == other.__dict__

    def __init__(self, title: str = None, author: str = None, page_count: int = None,
                 publication_date: datetime.date = None):
        """Initializes Book instance.

        :param title: Title of Book.
        :param author: Author of Book.
        :param page_count: Page Count of Book.
        :param publication_date: Publication Date of Book.
        """
        self.author = author
        self.page_count = page_count
        self.publication_date = publication_date
        self.title = title

    def __len__(self):
        """Returns the length of title."""
        return len(self.title)

    def __str__(self):
        """Returns a formatted string representation of Book."""
        date = '' if self.publication_date is None else f', published on {self.publication_date.__format__("%B %d, %Y")}'
        return f'\'{self.title}\' by {self.author} at {self.page_count} pages{date}.'

def check_equality(a, b):
    """Asserts the equivalent of the two passed objects.

    :param a: First object.
    :param b: Second object.
    :return: Indicates if assertion was successful.
    """
    try:
        logger.info("ASSERTING EQUIVALENCE OF...")
        # Output objects using __str__ method.
        logger.log(msg = f'a value is {a}', level = logging.INFO)
        logger.log(msg = f'b value is {b}', level = logging.INFO)
        # Assert equivalence of objects, indicating inequality if failed.
        assert a == b, "The objects ARE NOT equal."
        # Indicate that assertion succeeded.
        logger.log(msg = "The objects are equal.", level = logging.INFO)
        return True
    except AssertionError as error:
        # Output expected AssertionErrors.
        logger.exception(error)
    except Exception as exception:
        # Output unexpected Exceptions.
        logger.exception(exception, False)


if __name__ == '__main__':
    logger.info("BOTH INCLUDE PUBLICATION DATES")

    
    the_stand = Book("The Stand", "Stephen King", 1153, datetime.date(1978, 1, 1))
    the_stand_2 = Book("The Stand ", "Stephen King", 1153, datetime.date(1978, 1, 1))

    clean_code = Book("Clean Code", "Robert C. Martin", 500, datetime.date(1999, 6, 12))
    clean_architecture = Book("Clean Architecture", "Robert C. Martin", 350, datetime.date(1995, 5, 7))

    # Check equivalency of Books.
    check_equality(the_stand, the_stand_2)
    check_equality(clean_code, clean_architecture)

