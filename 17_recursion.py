def call_myself(n):
    print(f"I called mysef {n} times.")

    # exit condition
    if n == 10:
        return
    
    # recursion
    call_myself(n+1)

call_myself(1)