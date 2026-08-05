# Timer with Decorators
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution took {end - start:.3f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)

slow_function()


# Validation numbers with Decorators
def validate_number(func):
    def wrapper(*args):
        if not all(isinstance(a, (int,float)) for a in args):
            raise ValueError("All inputs must be numbers!")
        return func(*args)
    return wrapper

@validate_number
def add(a, b):
    return a + b

print(add(7, 12))


# Cache the output with decorator (Memoization)
def cache(func):
    saved = {}
    def wrapper(*args):
        if args in saved:
            return saved[args]
        result = func(*args)
        saved[args] = result
        return result
    return wrapper

@cache
def multiply(a, b):
    print("calculating...")
    return a * b

print(multiply(5, 4))
print(multiply(5, 4)) # cached