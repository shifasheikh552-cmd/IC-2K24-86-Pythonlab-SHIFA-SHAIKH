# Part B and Part C — Answers

## Part B: Predict the Output

### 1
```python
d = {"a": 1, "b": 2}
d2 = d
d2["c"] = 3
print(len(d))
```
**Output:** `3`

**Why:** `d2` and `d` refer to the same dictionary. Adding `"c"` through `d2` also changes `d`.

### 2
```python
d = {"x": [1]}
e = d.copy()
e["x"].append(2)
print(d)
```
**Output:** `{'x': [1, 2]}`

**Why:** `copy()` makes a shallow copy. The inner list is shared by both dictionaries.

### 3
```python
print({k: v for k, v in zip("abc", range(3)) if v})
```
**Output:** `{'b': 1, 'c': 2}`

**Why:** The condition `if v` excludes the value `0` because zero is false in a condition.

### 4
```python
d = {"a": 1}
print(d.setdefault("a", 9), d.setdefault("b", 5), d)
```
**Output:** `1 5 {'a': 1, 'b': 5}`

**Why:** `setdefault()` returns the existing value for `"a"` and inserts `"b": 5` because `"b"` was missing.

### 5
```python
d = {1: "a", 1.0: "b", True: "c"}
print(d, len(d))
```
**Output:** `{1: 'c'} 1`

**Why:** `1`, `1.0`, and `True` compare equal and have the same hash, so they refer to the same dictionary key. The value is overwritten each time.

### 6
```python
d = {"a": 1, "b": 2, "c": 3}
for k in d:
    if d[k] == 2:
        del d[k]
```
**Result:** `RuntimeError: dictionary changed size during iteration`

**Why:** A dictionary must not have keys added or removed while it is being iterated over.

### 7
```python
d = {"a": 1, "b": 2}
print(d.pop("z", None), d.popitem())
```
**Output:** `None ('b', 2)`

**Why:** `pop("z", None)` returns the default `None` because `"z"` is absent. `popitem()` removes and returns the last inserted key-value pair.

### 8
```python
print({v: k for k, v in {"a": 1, "b": 1}.items()})
```
**Output:** `{1: 'b'}`

**Why:** Both original items use value `1` as the new key. The second item overwrites the first value.

## Part C: Short Reasoning Questions

### 1. Why does `d2 = d` not create a copy? Difference between `copy()` and `deepcopy()`?
`d2 = d` makes another reference to the same dictionary; it does not create a new dictionary. A shallow copy (`d.copy()`) creates a new outer dictionary, but nested objects such as inner dictionaries and lists are still shared. A deep copy (`copy.deepcopy(d)`) recursively copies nested objects too. For a student database containing nested dictionaries, `deepcopy()` is useful when an independent full copy is required. If the program is only editing the original database directly, no copy is needed.

### 2. Why must dictionary keys be hashable? Which values can be keys?
Dictionary keys must be hashable so Python can calculate a stable hash and quickly locate the key. `[1, 2]` cannot be a key because a list is mutable. `(1, 2)` can be a key because this tuple contains immutable integers. `{1, 2}` cannot be a key because a set is mutable. `"12"` can be a key because strings are immutable and hashable.

### 3. When do we use `d[key]`, `d.get(key)` and `d.get(key, default)`?
- `d[key]`: use it when the key is expected to exist. It raises `KeyError` if it does not. Example: `students[roll]["name"]` after checking that `roll` exists.
- `d.get(key)`: use it when a missing key is acceptable and `None` is a suitable result. Example: `contacts.get(name)` when checking whether a contact exists.
- `d.get(key, default)`: use it when a useful fallback is needed. Example: `frequency[word] = frequency.get(word, 0) + 1` starts a new word at zero before adding one.

### 4. Difference between `.update()` and `d[key] = value`?
`d[key] = value` adds or replaces one key-value pair. `.update()` can add or replace several key-value pairs from another dictionary or an iterable of pairs in one operation. `.update()` is cleaner when several fields must be added or changed together.

### 5. Why is creating a new dictionary with a comprehension safer for the Q2 raise report?
A new dictionary keeps the original employee database unchanged. This is safer when the raise is only a report or a proposed calculation, because accidental changes do not affect the stored salaries. In-place modification is better when the intention is to permanently update the actual employee salary records.

### 6. Why does deleting keys while looping over a dictionary fail? Give two safe methods.
Deleting keys changes the dictionary's size while the loop is using its iterator, so Python raises a `RuntimeError`. Two safe methods are:
1. Loop over a copy of the keys: `for key in list(d): ...`
2. Build a new dictionary containing only the entries to keep: `d = {k: v for k, v in d.items() if condition}`

### 7. How do we invert book -> members into member -> books, and why use a list?
Loop through every book and every member in its `issued_to` list. For each member, add that book's title to a list using `setdefault(member, []).append(title)`. A list is needed because one member may hold more than one book.

### 8. Dictionary lookup time complexity vs searching a list?
A dictionary lookup is **O(1) on average**. Searching an unsorted list of records is **O(n)** because records may need to be checked one by one. In the phone directory, building a `number -> name` dictionary makes repeated reverse lookups much faster than scanning every contact and every phone number each time.
