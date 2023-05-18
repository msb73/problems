def goto(i: int):
    print(i)
    if i > 0:
        return goto(i-1)
    
goto(10)