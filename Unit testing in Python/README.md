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

## Skip/selectively run tests in pytest

Say we want to skip running the `test_calc_total` test for the moment

```python
import mathlib
import pytest

@pytest.mark.skip(reason="I am lazy")
def test_calc_total():
    total = mathlib.calc_total(4, 5)
    assert total == sum([4,5])

def test_calc_prod():
    prod = mathlib.calc_prod(4, 5)
    assert prod == 4*5
```

If we want to see the reason in the op log: `py.test -v -rxs`

```bash
PS C:\Users\shaun\Documents\my_projects\problem-solving-with-code\Unit testing in Python> py.test -v -rxs
===================================================================================== test session starts ===================================================================================== 
platform win32 -- Python 3.7.4, pytest-5.3.2, py-1.8.1, pluggy-0.13.1 -- c:\users\shaun\appdata\local\programs\python\python37\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\shaun\Documents\my_projects\problem-solving-with-code\Unit testing in Python
plugins: dash-1.9.0
collected 2 items                                                                                                                                                                               

test_mathlib.py::test_calc_total SKIPPED                                                                                                                                                 [ 50%] 
test_mathlib.py::test_calc_prod PASSED                                                                                                                                                   [100%] 

=================================================================================== short test summary info =================================================================================== 
SKIPPED [1] test_mathlib.py:4: I am lazy
================================================================================ 1 passed, 1 skipped in 2.07s =================================================================================
```

Sometimes we might want to skip a test if certain conditions are met. In that case we use the decorator: `pytest.mark.skipif`

```python
import mathlib
import pytest
import sys

@pytest.mark.skipif(sys.version_info < (3,5), reason="Python version > 3.5")
def test_calc_total():
    total = mathlib.calc_total(4, 5)
    assert total == sum([4,5])

def test_calc_prod():
    prod = mathlib.calc_prod(4, 5)
    assert prod == 4*5
```

```bash
PS C:\Users\shaun\Documents\my_projects\problem-solving-with-code\Unit testing in Python> py.test -v -rxs
===================================================================================== test session starts ===================================================================================== 
platform win32 -- Python 3.7.4, pytest-5.3.2, py-1.8.1, pluggy-0.13.1 -- c:\users\shaun\appdata\local\programs\python\python37\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\shaun\Documents\my_projects\problem-solving-with-code\Unit testing in Python
plugins: dash-1.9.0
collected 2 items                                                                                                                                                                               

test_mathlib.py::test_calc_total SKIPPED                                                                                                                                                 [ 50%] 
test_mathlib.py::test_calc_prod PASSED                                                                                                                                                   [100%] 

=================================================================================== short test summary info =================================================================================== 
SKIPPED [1] test_mathlib.py:5: Python version > 3.5
================================================================================ 1 passed, 1 skipped in 1.90s =================================================================================
```

### Run tests based on name

Say we want to run all tests which have "prod" in their names

`py.test -v -rxs -k prod`

```bash
PS C:\Users\shaun\Documents\my_projects\problem-solving-with-code\Unit testing in Python>  py.test -v -rxs -k prod
===================================================================================== test session starts ===================================================================================== 
platform win32 -- Python 3.7.4, pytest-5.3.2, py-1.8.1, pluggy-0.13.1 -- c:\users\shaun\appdata\local\programs\python\python37\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\shaun\Documents\my_projects\problem-solving-with-code\Unit testing in Python
plugins: dash-1.9.0
collected 2 items / 1 deselected / 1 selected                                                                                                                                                   

test_mathlib.py::test_calc_prod PASSED                                                                                                                                                   [100%] 

=============================================================================== 1 passed, 1 deselected in 1.32s ===============================================================================
```


## PyTest : Python Test Framework Tutorials

> https://www.youtube.com/playlist?list=PLFGoYjJG_fqoMMmCKLeLGQzh6Jz4CmO2Y

---


`py.test`

- this command will look for all files stating or ending with "test" in the project dir and run functions stating or ending with "test"

`py.test filename` 

- only execute tests in that file name

`py.test -k  login -v`

- execute tests with "login" in the function name