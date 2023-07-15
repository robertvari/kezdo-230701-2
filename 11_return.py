def add_numbers(a, b):
    return a+b

def divide_numbers(a, b):
    return a/b

def multiply_numbers(a, b):
    return a*b


add_result = add_numbers(10, 5)
divide_result = divide_numbers(100, add_result)
final_result = multiply_numbers(divide_result, 20)

print(f"The final result: {final_result}")