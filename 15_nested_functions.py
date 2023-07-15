def calculate_final(a, b):
    def add_numbers():
        return a+b

    def divide_numbers(add_result):
        return add_result/b

    def multiply_numbers(divide_result):
        return divide_result*b
    
    add_result = add_numbers()
    divide_result = divide_numbers(add_result)
    final_result = multiply_numbers(divide_result)

    return final_result

print(calculate_final(10, 5))