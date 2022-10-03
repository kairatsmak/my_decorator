import datetime
from time import sleep

def my_decorator(func):
    def wrapper(*args,**kwargs):
        start_date = datetime.datetime.now()
        func(*args,**kwargs)
        end_date = datetime.datetime.now()
        diff = end_date - start_date
        print(f'The function ({func.__name__}) elapsed time: {diff}')
    
    return wrapper

@my_decorator
def test_function(x, y):
    print("I am run!")
    sleep(5)
    print(x + y)

test_function(5, 5)