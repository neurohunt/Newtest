"""def add_all(*args):
    result = 0
    for num in args:
        result += num
    return result
    

print(add_all(1, 2, 3, 4, 5))


numbers = [1,2,3,4,5]
print(add_all(*numbers))
"""

"""def division(skaitlis1, skaitlis2):
    return skaitlis1/skaitlis2

print(division(skaitlis2 = 15,skaitlis1 = 5))"""



"""def greet(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key} : {value}")


greet(Firstname='John', Lastname='Doe', Age=25)"""

"""import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time to execute {func.__name__}: {end - start} seconds")
        return result
    return wrapper

@time_it
def count_to_n(n):
    for i in range(1, n+1):
        pass

count_to_n(10000000)
"""

"""
def log_decorator(func):
    def wrapper():
        print(f"Calling {func.__name__}")
        func()
        print(f"{func.__name__} finished execution")
    return wrapper"""

"""class BankAccount:

    def __init__(self):
        pass

    def papildin(func):
        def wrapper():
            print(f"Calling {func.__name__}")
            func()
            print(f"{func.__name__} ending")
        return wrapper
    
    @papildin
    def hello_world():
        print("Hello, world!")

newaccount = BankAccount()

newaccount.hello_world()
"""

"""
@log_decorator
def hello_world():
    print("Hello, world!")

hello_world()"""


"""
def repeat_decorator(num_times):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return actual_decorator

@repeat_decorator(3)
def greet(name):
    print(f"Hello, {name}")

greet("Alice")"""


""""class LogDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Calling {self.func.__name__}")
        result = self.func(*args, **kwargs)
        print(f"{self.func.__name__} finished execution")
        return result

@LogDecorator
def greet(name):
    print(f"Hello, {name}")

greet("Bob")"""


