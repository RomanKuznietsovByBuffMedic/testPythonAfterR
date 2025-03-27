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
        exec(code, {})


    cprint("-----------------------------------------\n" +
           "TEST " +
           chunk_title +
           "\n~~~~~~~~~~~~~~~",
                      
           "red")
    print_code_and_result(code)
    print("~~~~~~~~~~~~~~~\n")


# main

print_chunk_of_code("create lists", 
"""
# List of integers
print([45, 55, 32])

# List of strings
print(["Apples", "Oranges", "Bananas"])

# List of booleans
print([True, False, True])

# Empty List
print([])

# List of mixed data types
print([45, "Hello", True, 3.14])
""")

print_chunk_of_code("truthy and falsy lists",
"""
my_money = []
if my_money:
    print("I have some money!")
else:
    # this will be printed
    print("I have no money.")

your_money = [10, 10, 20, 1, 1]
if your_money:
    # this will be printed
    print("You have some money!")
else:
    print("You have no money.")
""")



print_chunk_of_code("lists in functions",
"""
def function(alpha: list[str]) -> list[int]:
    pass
""")


points = [1, 30, 9]
ordered_points = [1, 9, 30]
text_points = ["1", "9", "30"]

print("points == ordered_points is " + str(points == ordered_points))
print("points == text_points is " + str(points == text_points))
# add + -  * / **  with lists










names = ["Alice", "Bob", "Carol"]

print("Carol" in names)
# True

print("Ellie" in names)
# False

print("Car" in names)
# False

print("David" not in names)
# True