from Function_As_Object.func_as_obj import *


def test_return_result_of_factorial():
    """Expected result that function should return."""
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(5) == 120
    assert factorial(12) == 479001600


def test_func_obj_help_text():
    """The __doc__ attribute generates the help text of an object."""
    assert factorial.__doc__ == "returns n!"


def test_func_obj_can_assign_in_variable():
    """can be assigned in a variable and called through that name."""
    fact = factorial

    assert fact(1) == 1
    assert fact(4) == 24
    assert fact(5) == 120


def test_func_obj_can_pass_as_args_to_other_func():
    """Higher order function can take func_name as param and can apply the functionality on each element of the
    returned iterable sequences"""
    assert list(map(factorial, range(8))) == [1, 1, 2, 6, 24, 120, 720, 5040]

    unsorted_fact_list = [6, 1, 720, 120, 2, 1, 24]
    assert sorted(unsorted_fact_list, key=factorial) == [1, 1, 2, 6, 24, 120, 720]

    # Similar example to introduce Higher order function :: sorting a list of words bs length

    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

    assert sorted(fruits, key=len) == ['fig', 'apple', 'cherry', 'banana', 'raspberry', 'strawberry']


def test_map_filter_func_can_replace_with_list_comp():
    fact = factorial

    # Build a list of factorials from 0! to 5! with map(), while 2nd assertion does same with listcomp.

    assert list(map(fact, range(6))) == [1, 1, 2, 6, 24, 120]
    assert [fact(n) for n in range(6)] == [1, 1, 2, 6, 24, 120]

    # List of factorials of odd numbers up to 5!, using both map and filter. 2nd Assertion does the same job with
    # listcomp with no map and filter, and making lambda unnecessary.

    assert list(map(fact, filter(lambda n: n % 2, range(6)))) == [1, 6, 120]
    assert [fact(n) for n in range(6) if n % 2] == [1, 6, 120]
