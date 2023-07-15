def variable_length_keyword_arguments(**kwargs):
    print(kwargs, type(kwargs))

variable_length_keyword_arguments(
    name="Robert", 
    email="robert@gmail.com", 
    address="Budapest",
    password="testpas123",
    phone="06 20 12345678"
)