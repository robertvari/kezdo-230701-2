from my_functions.get_all_files import get_all_files

def call_myself(n):
    print(f"I called mysef {n} times.")

    # exit condition
    if n == 10:
        return
    
    # recursion
    call_myself(n+1)

my_files = []
get_all_files(
    root_folder=r"D:\Work\_PythonSuli\kezdo-230701\alapok2\test_recursion", 
    file_list=my_files
)