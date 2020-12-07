# Python Tips Collection

## 01.Merge Two Dicts

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# using the **kwargs
dict3 = {**dict1, **dict2}
print(dict3)
# Returns: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Python 3.9 --- |
dict3 = dict1 | dict2
```

## 02.Use Get Instead of the Dictionary Accessor

