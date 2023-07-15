def variable_length_args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

variable_length_args_kwargs(
    1,
    2,
    3,
    "Csaba",
    "Kriszta",
    email="csaba@gmail.com",
    address="Békéscsaba"
)