"""
Run multiple functions as tests with continuing even if it fails
"""

def test_one():
    print("one")
    assert(0)

def test_two():
    print("two")
    assert(0)

def test_three():
    print("Three")

def main():
    tests = [test_one, test_two, test_three]
    for test in tests:
        try:
            test()
        except:
            print(f"Test {test} failed")