import pytest

from chapter5 import clear_bit, get_bit, set_bit, update_bit, binary_to_int, int_to_binary
from chapter5 import problem1, problem2, problem3, problem5, problem6


def test_should_get_bit():
    assert get_bit(9,0)
    assert not get_bit(9,1)
    assert not get_bit(9,2)
    assert get_bit(9,3)


def test_set_bit():
    num = set_bit(9, 1)
    assert num == 11


def test_clear_bit():
    eight = clear_bit(9, 0)
    assert eight == 8
    one = clear_bit(9, 3)
    assert one == 1


def test_update_bit():
    eight = update_bit(9, 0, 0)
    eleven = update_bit(9, 1, 1)
    assert eight == 8
    assert eleven == 11


def test_binary_to_int():
    assert binary_to_int('1000') == 8
    assert binary_to_int('111') == 7


def test_int_to_binary():
    assert int_to_binary(8) == '1000'
    assert int_to_binary(15) == '1111'


def test_problem1():
    result = problem1(binary_to_int('10000000000'), binary_to_int('10011'), 2, 6)
    assert int_to_binary(result) == '10001001100'

    result = problem1(binary_to_int('11111111'), binary_to_int('010'), 1, 3)
    assert int_to_binary(result) == '11110101'


def test_problem2():
    assert problem2(.6875) == '.1011'
    assert problem2(.16) == 'ERROR'
    assert problem2(.67041015625) == '.10101011101'


def test_problem3():
    int_value = binary_to_int('11011001111100')
    next_largest, next_smallest = problem3(int_value)
    assert int_to_binary(next_largest) == '11011010001111'
    assert int_to_binary(next_smallest) == '11011001111001'


def test_problem5():
    assert problem5(31, 14) == 2


def test_problem6():
    int_value = binary_to_int('100110011001')
    swapped = problem6(int_value)
    assert int_to_binary(swapped) == '11001100110'
    int_value = binary_to_int('010001110001')
    swapped = problem6(int_value)
    assert int_to_binary(swapped) == '100010110010'

