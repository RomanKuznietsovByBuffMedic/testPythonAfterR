print("Hello, World!")
print("ah shit, here we go again")



msg = "I'm so tired"
print(msg)



# https://pypi.org/project/numpy/
import numpy as np

print(np.random.rand(1, 3))



print(1 < 2 and 2)



_1 = 1
print("_1 = ", _1)






m = "#3" #4
print(m)






print("abc" < "abd")
print("a" > "A")
print("z" > "abc")






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






print("1" == 1)
# print(12 in 123) # TypeError





 
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
 





hour = 7

# with `hour <=6` 
# variable `time` will not be initialized
# and this make an error

if hour > 6:
    time = "It is dayligtht"

print(time)






# This is False because True is not equal to 5
print(True == 5)

# This is True because 5 is Truthy
print(True == bool(5))






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
