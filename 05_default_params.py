def say_hello(name, email=None, address=None):
    print(f"Hello {name}")

    if email:
        print(f"Your email is: {email}")

    if address:
        print(f"Your address is: {address}")


say_hello("Csaba", "csaba@gmail.com", "Budapest")