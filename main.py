# import my_package.functions
# import my_package.constants

# my_package.functions.greet(my_package.constants.PERSON)

from my_package.functions import greet
from my_package.constants import PERSON

greet(PERSON)
