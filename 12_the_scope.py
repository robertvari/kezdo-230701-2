# GLOBAL variable
NAME = "Kriszta"

def print_hello():
    # LOCAL variable
    name = "Csaba"
    print(f"Hello {name}")
    print(f"Hello {NAME}")

def my_function():
    print(f"my_function: {NAME}")

print_hello()
my_function()