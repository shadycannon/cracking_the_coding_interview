#!/usr/bin/python3
import math
from typing import Dict, Generator, List, Optional, Tuple


def get_bit(num: int, i: int) -> int:
    bit = num & (1 << i)
    if bit:
        return 1
    return 0


def set_bit(num: int, i: int) -> int:
    num = num | (1 << i)
    return num


def clear_bit(num: int, i: int) -> int:
    num = num & (~(1 << i))
    return num


def update_bit(num: int, i: int, value: int) -> int:
    if value not in [0, 1]:
        return num
    mask = ~(1 << i)
    num = num & mask
    return num | (value << i)


def binary_to_int(b: str) -> int:
    return int(b, 2)


def int_to_binary(i: int) -> str:
    return str(bin(i))[2:]


def problem1(n: int, m: int, i: int, j: int) -> int:
    """You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method to
    insert M into N such that M starts at bit j and ends at but i. You can assume that the bits j though i
    have enough bits to fit all of M
    ex: N = 10000000000, M = 10011, i = 2, j = 6 -> 10001001100"""
    # mask off i through j on N
    # shift M i to the left
    # combine
    all_ones = ~0
    mask = all_ones << j + 1
    end_mask = ~(all_ones << i)
    mask = mask | end_mask
    n = n & mask
    m = m << i
    return n | m


def problem2(num: float) -> str:
    """Given a real number between 0 and 1 (e.g. .72) that is passed in as a float,
    print the binary representation. If the number cannot be printed accurately in binary with
    at most 32 characters, print "ERROR"""
    binary_repr = '.'
    for _ in range(0, 32):
        num = num * 2
        if num == 1:
            return binary_repr + '1'
        if num > 1:
            binary_repr += '1'
            num -= 1
        else:
            binary_repr += '0'

    return 'ERROR'


def find_next_biggest(num: int) -> int:
    temp = num
    switch_index = 0
    while not temp & 1:
        switch_index += 1
        temp = temp >> 1

    one_count = 0
    while temp & 1:
        one_count += 1
        temp = temp >> 1
        switch_index += 1


    num = set_bit(num, switch_index)
    print(int_to_binary(num))
    mask = ~ ((1 << switch_index) - 1)

    one_mask = (1 << (one_count - 1)) - 1
    num = mask & num

    return num | one_mask


def find_next_smallest(num: int) -> int:
    temp = num
    switch_index = 0
    trailing_ones = 0
    while temp & 1:
        switch_index += 1
        trailing_ones += 0
        temp = temp >> 1
    trailing_zeros = 0
    while not temp & 1:
        switch_index += 1
        trailing_zeros += 1
        temp = temp >> 1
    mask = 1 << switch_index
    num = num ^ mask

    one_mask = 1 << trailing_ones
    return num | one_mask


def problem3(num: int) -> Tuple[int, int]:
    """Given a positive integer, print the next smallest and the next largest number
    that have the same number of 1 bits in their binary representation"""
    return find_next_biggest(num), find_next_smallest(num)


def problem5(a: int, b: int) -> int:
    """Write a function to determine the number of bits required to convert int A to int B
    ex. input: 31 & 14 -> 2"""
    diff = a ^ b
    count = 0
    while diff:
        if diff & 1:
            count += 1
        diff = diff >> 1
    return count


def problem6(num: int) -> int:
    """Write a problem to swap odd and even bits in an integer with as few
    instructions as possible. e.g. bit 0 and bit 1 are swapped, bit 2 and bit3 are swapped, etc. etc. """
    odd_mask = binary_to_int('01010101010101010101010101010101')
    even_mask = binary_to_int('10101010101010101010101010101010')
    odds = num & odd_mask
    odds = odds << 1
    evens = num & even_mask
    evens = evens >> 1
    return odds | evens


def problem7():
    """An array A contains all the integers from 0 to n, except for one number which is
    missing. In this problem, we cannot access an entire integer in A with a single operation.
    The elements of A are represented in binary, and the only operation we can use to access them
     is "fetch the jth bit of A[i]," which takes constant time. Write code to find the missing integer in O(n)"""