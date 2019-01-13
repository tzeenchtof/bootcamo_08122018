import time

start = time.time()
lista = [x*2 for x in range(1000000)]
stop = time.time()

print (start-stop)

def baz():
    pass


def foo(bar):
    print(bar.__name__)

print(dir(print))
foo(print)

def log(funkcja):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = funkcja(*args, **kwargs)
        stop = time.time()
        duration = stop-start
        print(f'długość wywołania {funkcja.__name__} to {duration}s')
        return result
    return wrapper

# zaimplementuj dekorator wypisujący wywołanie danej funkcji
# (nazwa i argumenty) oraz czas jej wykonania
# przykład użycia
#



@log
def foo(arg):
    return f'to jest {arg}'

def test_decorated_foo():
    assert "Długość wywołania foo" in foo(1)