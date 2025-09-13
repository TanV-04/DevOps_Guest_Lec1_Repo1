from app import add

def test_add():
    assert add(2, 3) == 5

#this is a unit test function
# pytest looks for any function that starts with test_.
# If add(2, 3) equals 5, the test passes.
# If not, the test fails and pytest reports an error.