# define functions

# for better print code and result of code
def print_chunk_of_code(chunk_title: str, code: str) -> None:
    '''
    This function prints the `chunk_title`, the `code` and the result `code`.

    Args:
        str (chunk_title): The chunk title of the code.
        str (code): The code to execute.
    Returns:
        None
    '''


    # https://pypi.org/project/termcolor/
    from termcolor import colored, cprint


    def print_code_and_result(code: str) -> None:
        '''
        This function prints the `code` and the result of the `code`.

        Args:
            str (code): The code to execute.
        Returns:
            None
        '''
        print(colored("Code:", "green"), code)
        cprint("Result:", "blue")
        exec(code)


    cprint("-----------------------------------------\n" +
           "TEST " +
           chunk_title +
           "\n~~~~~~~~~~~~~~~",
                      
           "red")
    print_code_and_result(code)
    print("~~~~~~~~~~~~~~~\n")


# main

print_chunk_of_code("`print()`",
"""
print("Hello, World!")
print("Ah shit, here we go again")
""")



print_chunk_of_code("variable",
"""
msg = "I'm so tired"
print(msg)
""")



print_chunk_of_code("`import`",
"""
# https://pypi.org/project/numpy/
import numpy as np

print(np.random.rand(1, 3))
""")



print_chunk_of_code("boolean expression",
"""
print(1 < 2 and 2)
""")



print_chunk_of_code("name what start with _",
"""
_1 = 1
print("_1 = ", _1)
""")



print_chunk_of_code("comment in string",
"""
m = "#3" #4
print(m)
""")



print_chunk_of_code("string comparison",
"""
print("abc" < "abd")
print("a" > "A")
print("z" > "abc")
""")



print_chunk_of_code("`[]`",
"""
word = "hamster"

print("first subsection")
print(word[0])
print(word[-0])

print("second subsection")
print(word[-1])
print(word[1:-1])

print("third subsection")
print(word[-3:])
print(word[:3])
""")



print_chunk_of_code("type importance",
"""
print("1" == 1)
# print(12 in 123) # TypeError
""")



print_chunk_of_code("unit tests by `assert_equal()`",
""" 
# https://github.com/python-bakery/bakery-support-library
from bakery import assert_equal

def calculate_area(length: int, width: int) -> int:
    '''
    This function calculates the area of a rectangle based on its dimensions. 
    
    Args:
        length (int): The length of the rectangle in feet.
        width (int): The width of the rectangle in feet.
    Returns:
        int: The area in square feet.
    '''
    area = length * width
    return area

assert_equal(calculate_area(5, 6), 30)
assert_equal(calculate_area(0, 6), 0)
assert_equal(calculate_area(4, 5), 21)
""") 



print_chunk_of_code("initialize in `if`",
"""
hour = 7

# with `hour <=6` 
# variable `time` will not be initialized
# and this make an error

if hour > 6:
    time = "It is day light"

print(time)
""")



print_chunk_of_code("truthy values",
"""
# This is False because True is not equal to 5
print(True == 5)

# This is True because 5 is Truthy
print(True == bool(5))
""")



print_chunk_of_code("easy way to create a class by `dataclass`",
"""
# Required import
from dataclasses import dataclass

# Definition
@dataclass
class Box:
    width: int
    length: int


# Instance creation
my_box = Box(5, 10)

# Using the instance
print(my_box)
""")




print_chunk_of_code("test change value of `dataclass`",
"""
from dataclasses import dataclass

@dataclass
class Dog:
    name: str
    age: int
    is_fuzzy: bool

ada = Dog("Ada Bart", 4, True)
print("Ada's name is", ada.name)

ada.name = "adam"
print("Ada's name is", ada.name)
""")


