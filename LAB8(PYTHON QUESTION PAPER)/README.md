# Python Programming: Advanced Question Paper 

# SECTION A: Technical Questions 

## Q1. Boolean-to-integer coercion

**Output**
```
2
8
-5
True
False
```

**Step-by-step evaluation**

| Line | Evaluation | Result |
|---|---|---|
| `True + True` | `1 + 1` | `2` |
| `True * 8` | `1 * 8` | `8` |
| `False - 5` | `0 - 5` | `-5` |
| `0 == False` | `0 == 0` | `True` |
| `2 == True` | `2 == 1` | `False` |

**Explanation:** `bool` is a **subclass of `int`**, with `True == 1` and `False == 0`. In arithmetic and comparison, the boolean is used as the integer 1 or 0. `2 == True` is False because 2 is not equal to 1, even though `bool(2)` is True. Equality compares values, not truthiness.



## Q2. `is` vs `==` 

**Output**
```
True
True
False
True
```

**Difference**
- `==` tests **equality of value** (calls `__eq__`).
- `is` tests **identity**: whether both names refer to the **same object** (same `id()`).

**Trace**

| Step | State | `b is a` | `b == a` |
|---|---|---|---|
| `b = a` | one list object, two names (`a`, `b`) | True | True |
| `b = [1, 2, 3, 4]` | a **new** list object is created and `b` is rebound; `a` still points to the old list | False | True |

After reassignment the two lists hold equal contents (so `==` is True) but are **two distinct objects** (so `is` is False).


## Q3. Floor division and modulo 

**Output**
```
1
-2
1.0
2
-2
```

**Step-by-step evaluation** (Python defines `a % b = a - b * (a // b)`, with `//` = floor)

| Expression | Calculation | Result |
|---|---|---|
| `5 // 3` | floor(1.67) | `1` |
| `-5 // 3` | floor(-1.67) | `-2` |
| `5.0 // 3.0` | floor(1.67), float operands give a float | `1.0` |
| `-7 % 3` | `//` gives floor(-2.33) = -3, so -7 - 3(-3) = -7 + 9 | `2` |
| `7 % -3` | `//` gives floor(-2.33) = -3, so 7 - (-3)(-3) = 7 - 9 | `-2` |

**Why `-7 % 3` is 2 in Python but -1 in C:** Python's `//` **floors toward negative infinity**, and `%` is defined so that `a == (a // b) * b + a % b` always holds. C (C99 and later) **truncates toward zero**, so `-7 / 3 = -2`, and the remainder is -7 - (-2)(3) = **-1**.

**Rule:** in Python the result of `%` has the **same sign as the divisor** (and `0 <= r < b` when `b > 0`). In C the remainder has the sign of the dividend.

---

## Q4. Slicing 

```python
li = [1, 2, 4, 3]
li[1:3]    # (a) [2, 4]
li[2:]     # (b) [4, 3]
li[:3]     # (c) [1, 2, 4]
li[::2]    # (d) [1, 4]
li[::-1]   # (e) [3, 4, 2, 1]
```

**Syntax:** `li[start:end:step]`
- `start` is inclusive (default 0), `end` is **exclusive** (default `len(li)`), `step` defaults to 1.
- Slicing returns a **new list**, so `li` is not modified.

**Negative step:** traversal goes **right to left**. The defaults for `start` and `end` swap (start at the last element, go to the first). `li[::-1]` reverses the list. With explicit bounds `start` must be greater than `end`, e.g. `li[3:0:-1]` gives `[3, 4, 2]`.

---

## Q5. Tuple and extended unpacking 

```python
a, b, c = (1, 2, 3)        # a=1, b=2, c=3
a, *b, c = (1, 2, 3, 4)    # a=1, b=[2, 3], c=4
print(type((1)))           # <class 'int'>
print(type((1,)))          # <class 'tuple'>
```

- **Tuple unpacking:** the elements are assigned to the names **by position**; the number of names must equal the number of elements.
- **Extended unpacking:** one starred name (`*b`) takes all the **leftover** elements. `a` gets the first and `c` the last element.
- **Type of `b`:** `list` (`[2, 3]`). A starred target always collects into a **list**, even when the source is a tuple.
- **`(1)` vs `(1,)`:** parentheses alone only group an expression, so `(1)` is the integer `1`. A tuple is created by the **comma**, so a one-element tuple must be written `(1,)`.

---

## Q6. Closure and `nonlocal` 

**Output**
```
3.0
4.0
5.0
```

**Trace**

| Call | `total` | `count` | Returns |
|---|---|---|---|
| `create_avg()` | 0 | 0 | the function `avg` (closure keeps `total` and `count`) |
| `avg(3)` | 0 + 3 = 3 | 1 | 3 / 1 = **3.0** |
| `avg(5)` | 3 + 5 = 8 | 2 | 8 / 2 = **4.0** |
| `avg(7)` | 8 + 7 = 15 | 3 | 15 / 3 = **5.0** |

(`/` is true division, so the results are floats.)

**Without `nonlocal`:** `total += n` is an assignment, so Python treats `total` and `count` as **local** to `avg`. The first call then reads `total` before it has a value, raising **`UnboundLocalError`**. `nonlocal` makes the assignment rebind the variables in the enclosing scope.

**Closure vs regular nested function:** a **closure** is a nested function that **captures and remembers variables from its enclosing scope** even after the outer function has returned (here `total` and `count`, stored in `avg.__closure__`). A regular nested function does not use enclosing variables, so it carries no such state.

---

## Q7. `*args` and `**kwargs` [4]

**Role**
- `*args` in a definition **packs** extra positional arguments into a **tuple**.
- `**kwargs` in a definition **packs** extra keyword arguments into a **dict**.
- In a call, `*seq` **unpacks** a sequence into positional arguments, and `**dict` unpacks a dict into keyword arguments.

**Output** (each call prints `args` then `kwargs`)

Call 1, `all_the_args(*args)` is the same as `all_the_args(1, 2, 3, 4)`:
```
(1, 2, 3, 4)
{}
```
Call 2, `all_the_args(**kwargs)` is the same as `all_the_args(a=3, b=4)`:
```
()
{'a': 3, 'b': 4}
```
Call 3, `all_the_args(*args, **kwargs)` is the same as `all_the_args(1, 2, 3, 4, a=3, b=4)`:
```
(1, 2, 3, 4)
{'a': 3, 'b': 4}
```
---

## Q8. Set operations 

```python
A = {1, 2, 3, 4}
B = {2, 3, 5}
```

| Expression | Set-theory operation | Qualifying elements | Output |
|---|---|---|---|
| `A & B` | intersection | in **both** A and B | `{2, 3}` |
| `A \| B` | union | in A **or** B (or both) | `{1, 2, 3, 4, 5}` |
| `A - B` | difference | in A but **not** in B | `{1, 4}` |
| `A ^ B` | symmetric difference | in **exactly one** of A, B | `{1, 4, 5}` |
| `{1,2} <= {1,2,3}` | subset (improper) | every element of `{1,2}` is in `{1,2,3}` | `True` |

**`{[1,2,3]: 'abc'}` vs `{(1,2,3): 'abc'}`:** dictionary keys (and set elements) must be **hashable**, meaning they have a hash value that never changes. A **list is mutable**, so it is unhashable and raises `TypeError: unhashable type: 'list'`. A **tuple of immutable elements** is immutable and hashable, so it is a valid key.

---

## Q9. Decorator with `@wraps` 

**Calling `my_function(1, 2)`** prints:
```
Entering my_function
Exiting my_function
```
(The return value 3 is not printed, because the call is not inside `print`.)

**(a) Without `@wraps(func)`:**
```
wrapper
None
```
`@log_function` is shorthand for `my_function = log_function(my_function)`. The name `my_function` is therefore bound to the inner **`wrapper`** function, so `__name__` is `'wrapper'`. `wrapper` has no docstring, so `__doc__` is `None`. (The "Entering" message still shows `my_function`, because it reads `func.__name__` from the original function.)

**(b) With `@wraps(func)`:**
```
my_function
Adds two numbers together.
```
`functools.wraps` copies the metadata (`__name__`, `__doc__`, `__module__`, `__qualname__`, and updates `__dict__`) from `func` to `wrapper`, and sets `wrapper.__wrapped__ = func`. The decorated function therefore keeps its identity for `help()`, debugging and introspection.

**(c) Equivalent without `@` syntax:**
```python
def my_function(x, y):
    '''Adds two numbers together.'''
    return x + y

my_function = log_function(my_function)
```

---

## Q10. Multiple inheritance (`Batman`) 

**(a) MRO** (computed by C3 linearization)
```
(<class '__main__.Batman'>, <class '__main__.Superhero'>, <class '__main__.Human'>, <class '__main__.Bat'>, <class 'object'>)
```
i.e. `Batman -> Superhero -> Human -> Bat -> object`. `Superhero` is a subclass of `Human`, so `Human` must come after `Superhero`, and `Bat` is listed after because of the base order `(Superhero, Bat)`.

**(b)** `sup.say('I agree')` invokes **`Human.say`** and returns `Sad Affleck: I agree`.
Python searches for the method along the MRO: `Batman` (no `say`), then `Superhero` (no `say`), then **`Human` (has `say`, found, search stops)**. `Bat.say` (which would return `'... ... ...'`) comes later in the MRO and is never reached. If the bases were written `(Bat, Superhero)`, `Bat.say` would win.

**(c)** Reasons both `__init__` methods are called explicitly:
1. `super()` only moves to the **next class in the MRO**. `Superhero.__init__` calls `super().__init__(...)`, which reaches `Human.__init__`. `Human.__init__` does **not** call `super().__init__()`, so the chain stops there and `Bat.__init__` would never run.
2. The two parents take **different arguments** (`name`, `movie`, `superpowers` for `Superhero`; `can_fly` for `Bat`), so one cooperative `super()` call cannot give each its own set.
3. Calling `Bat.__init__(self, *args, can_fly=False, **kwargs)` explicitly makes sure `Bat` is initialized and that `self.fly` is set to `False`.

---

# SECTION B: Theoretical Questions 

## Q11. Generators in Python 

**(a) What a generator is, and how it differs from a function returning a list [1]**
A generator is a special **iterator** produced by a function containing `yield` (or by a generator expression). Calling it does not run the body; it returns a generator object that produces values **lazily**.

| | Function returning a list | Generator |
|---|---|---|
| Values | all computed **at once** | produced **one at a time, on demand** |
| Memory | whole list stored | only the current value and local state |
| Reuse | list can be iterated repeatedly | **single-use**; exhausted after one pass |
| Indexing / `len()` | supported | not supported |

**(b) The `yield` keyword and preserved state [1]**
`yield value` returns `value` to the caller and **suspends** the function, **keeping its local variables, loop position and instruction pointer**. The next `next()` call (or loop iteration) **resumes immediately after the `yield`**. When the function finishes, `StopIteration` is raised, which ends the `for` loop.

**(c) Memory efficiency using the example [1]**
```python
def double_numbers(iterable):
    for i in iterable:
        yield i + i

for i in double_numbers(range(1, 900000000)):
    print(i)
    if i >= 30:
        break
```
Output: `2, 4, 6, ..., 30` (one per line, 15 values; the loop breaks when `i` reaches 30).
Each value is created only when requested, and `range` in Python 3 is also lazy. At any moment only **one** number exists in memory, and the generator is abandoned after 15 items. Building the same result as a list would mean creating 900 million integers first, which needs tens of gigabytes. The generator needs a constant, tiny amount of memory.

**(d) Generator function vs generator comprehension [1]**
```python
# Generator function: uses def and yield, may contain multiple statements
def squares(n):
    for i in range(n):
        yield i * i

# Generator comprehension (expression): one line, round brackets, no yield keyword
gen = (i * i for i in range(5))
```
Both are lazy and single-use. A function suits complex logic, several `yield`s or kept state. A comprehension suits a simple transform or filter on one iterable.

**(e) When to prefer a generator over a list [1]**
- Very large or **infinite** sequences (e.g. Fibonacci numbers).
- **Streaming** data, such as reading a large file line by line.
- **Pipelines** where each stage feeds the next without storing intermediate lists.
- When the consumer may **stop early** (`break`, `any()`, `next()`).

Prefer a list when you need random access, `len()`, slicing, or several passes over the data.

---

## Q12. Python's OOP model (`Human` and `Superhero`) [5]

```python
class Human:
    species = "H. sapiens"                 # class attribute
    def __init__(self, name):
        self.name = name                   # instance attribute
        self._age = 0                      # "internal" attribute

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def grunt():
        return "*grunt*"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @age.deleter
    def age(self):
        del self._age
```

**(a) Instance vs class attributes [1]**
- **Instance attributes** (`self.name`, `self._age`) are created per object, usually in `__init__`; each instance has its own copy. Access: `h.name`.
- **Class attributes** (`species`) are defined in the class body and are **shared by all instances**. Access: `Human.species` or `h.species`.
- Assigning `h.species = "X"` creates an **instance attribute that shadows** the class attribute and does not change `Human.species`.

**(b) `@classmethod`, `@staticmethod`, `@property` [1]**

| Decorator | First argument | Purpose | Example from `Human` |
|---|---|---|---|
| `@classmethod` | the class (`cls`) | works with class-level data; callable on the class or an instance | `Human.get_species()` returns `"H. sapiens"` |
| `@staticmethod` | none | plain function grouped inside the class; no access to `self` or `cls` | `Human.grunt()` returns `"*grunt*"` |
| `@property` | `self` | method accessed like an attribute, without `()` | `h.age` returns `h._age` |

**(c) `super()` in single and multiple inheritance [1]**
- **Single inheritance:** `super()` returns a proxy that delegates to the **parent class**, so `super().__init__(name)` runs the parent's initializer without naming the parent explicitly (as `Superhero` does with `Human`).
- **Multiple inheritance:** `super()` follows the **MRO** and moves only to the **next** class in it, not to all parents. It falls short because (i) a parent that does not call `super().__init__()` breaks the chain, so later parents are never initialized (as with `Human` and `Bat`), and (ii) parents with different `__init__` signatures cannot all be served by one `super()` call. Explicit calls such as `Bat.__init__(...)` are then needed.

**(d) `_age` convention and encapsulation with properties [1]**
- A **single leading underscore** (`_age`) is only a **naming convention** meaning "internal, do not access directly". Python has **no `private` keyword** and does not enforce it. (A double underscore triggers name mangling but is also not true privacy.)
- `@property` defines the **getter** (`h.age`), `@age.setter` defines the **setter** (`h.age = 5`), and `@age.deleter` defines the **deleter** (`del h.age`). Reads, writes and deletes of `age` go through methods, so you can add validation or computation later while the public interface stays `h.age`. That is encapsulation without `private`.

**(e) `if __name__ == '__main__':` [1]**
`__name__` is set to `'__main__'` when the file is **run directly**, and to the **module's name** when it is **imported**. The guard makes the enclosed code (demos, tests, program start-up) run **only on direct execution**. Importing the module then gives access to its classes and functions **without side effects**, which makes it reusable.

---

