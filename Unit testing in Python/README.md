# Unit testing in Python

Based on the tutorial by **CodeBasics**: [https://www.youtube.com/watch?v=l32bsaIDoWk](https://www.youtube.com/watch?v=l32bsaIDoWk)

## Introduction

### Setting up

**File: `mathlib.py`**

```python
def calc_total(a,b):
    return a+b
def calc_prod(a,b):
    return a*b
```

Any file for pytest has to have the "*test_*" prefix

Create file `test_mathlib.py`

```python
import mathlib
def test_calc_total():
    total = mathlib.calc_total(4, 5)
    assert total == sum(4,9)

def test_calc_prod():
    prod = mathlib.calc_product(4, 5)
    assert prod == 4*5
```

`test_calc_total` and `test_calc_prod` are basically our unit tests

It is important that the unit test file and unit test functions both start with "test_"

### Running the tests

Now navigate to this directory

Run: `python -m pytest`

**💡This will recursively go into all files and sub directories and look for file starting with "test_" and in that file execute all functions with "test_"**

We get the output:

```bash
====================================================================================== 2 passed in 0.93s ======================================================================================
```

Another way of running: `py.test`

Does the same as above

For a more verbose output: `py.test - v`

```bash
===================================================================================== test session starts ===================================================================================== 
platform win32 -- Python 3.7.4, pytest-5.3.2, py-1.8.1, pluggy-0.13.1 -- c:\users\shaun\appdata\local\programs\python\python37\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\shaun\Documents\my_projects\problem-solving-with-code\Unit testing in Python
plugins: dash-1.9.0
collected 2 items                                                                                                                                                                               

test_mathlib.py::test_calc_total PASSED                                                                                                                                                  [ 50%] 
test_mathlib.py::test_calc_prod PASSED                                                                                                                                                   [100%] 

====================================================================================== 2 passed in 1.89s ======================================================================================
```

This is a useful way of finding which functions (tests) were actually executed