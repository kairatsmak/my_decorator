import datetime
from time import sleep

def my_decorator(func):
    start_date = datetime.datetime.now()
    func()
    end_date = datetime.datetime.now()
    diff = end_date - start_date
    print(f'The function ({func.__name__}) elapsed: {diff}')

@my_decorator
def test_function():
    print("I am run!")
    sleep(5)
