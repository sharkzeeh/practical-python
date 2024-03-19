# pytest_simple.py

import simple

def test_simple():
    assert simple.add(2, 2) == 4

def test_str():
    assert simple.add('hello', 'world') == 'helloworld'

# python3 -m pytest                    -- runs all test files
# python3 -m pytest ./pytest_simple.py -- runs on a single file
