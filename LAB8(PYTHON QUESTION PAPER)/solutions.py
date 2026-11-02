
from functools import wraps

# Q1
assert (True + True, True * 8, False - 5, 0 == False, 2 == True) == (2, 8, -5, True, False)

# Q2
a = [1, 2, 3, 4]; b = a
assert (b is a, b == a) == (True, True)
b = [1, 2, 3, 4]
assert (b is a, b == a) == (False, True)

# Q3
assert (5 // 3, -5 // 3, 5.0 // 3.0, -7 % 3, 7 % -3) == (1, -2, 1.0, 2, -2)

# Q4
li = [1, 2, 4, 3]
assert (li[1:3], li[2:], li[:3], li[::2], li[::-1]) == ([2, 4], [4, 3], [1, 2, 4], [1, 4], [3, 4, 2, 1])

# Q5
x, *y, z = (1, 2, 3, 4)
assert y == [2, 3] and type((1)) is int and type((1,)) is tuple

# Q6
def create_avg():
    total = 0
    count = 0
    def avg(n):
        nonlocal total, count
        total += n
        count += 1
        return total / count
    return avg

avg = create_avg()
assert (avg(3), avg(5), avg(7)) == (3.0, 4.0, 5.0)

# Q7
def all_the_args(*args, **kwargs):
    return args, kwargs

args = (1, 2, 3, 4); kwargs = {'a': 3, 'b': 4}
assert all_the_args(*args) == ((1, 2, 3, 4), {})
assert all_the_args(**kwargs) == ((), {'a': 3, 'b': 4})
assert all_the_args(*args, **kwargs) == ((1, 2, 3, 4), {'a': 3, 'b': 4})

# Q8
A = {1, 2, 3, 4}; B = {2, 3, 5}
assert (A & B, A | B, A - B, A ^ B) == ({2, 3}, {1, 2, 3, 4, 5}, {1, 4}, {1, 4, 5})
assert {1, 2} <= {1, 2, 3}
try:
    {[1, 2, 3]: 'abc'}
except TypeError:
    pass
else:
    raise AssertionError("expected TypeError")

# Q9
def log_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Entering', func.__name__)
        result = func(*args, **kwargs)
        print('Exiting', func.__name__)
        return result
    return wrapper

@log_function
def my_function(x, y):
    '''Adds two numbers together.'''
    return x + y

my_function(1, 2)
assert my_function.__name__ == 'my_function'
assert my_function.__doc__ == 'Adds two numbers together.'

# Q10
class Human:
    species = "H. sapiens"
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self._age = 0
    def say(self, msg):
        return "{name}: {message}".format(name=self.name, message=msg)

class Superhero(Human):
    species = "Superhuman"
    def __init__(self, *args, **kwargs):
        self.fictional = kwargs.pop('movie', False)
        self.superpowers = kwargs.pop('superpowers', [])
        super().__init__(*args, **kwargs)

class Bat:
    species = 'Baty'
    def __init__(self, *args, can_fly=True, **kwargs):
        self.fly = can_fly
        super().__init__(*args, **kwargs)
    def say(self, msg):
        return '... ... ...'

class Batman(Superhero, Bat):
    def __init__(self, *args, **kwargs):
        Superhero.__init__(self, 'anonymous', movie=True,
                           superpowers=['Wealthy'], *args, **kwargs)
        Bat.__init__(self, *args, can_fly=False, **kwargs)
        self.name = 'Sad Affleck'

assert Batman.__mro__ == (Batman, Superhero, Human, Bat, object)
sup = Batman()
assert sup.say('I agree') == 'Sad Affleck: I agree'

# Q11
def double_numbers(iterable):
    for i in iterable:
        yield i + i

out = []
for i in double_numbers(range(1, 900000000)):
    out.append(i)
    if i >= 30:
        break
assert out == list(range(2, 31, 2))

print("All checks passed.")
