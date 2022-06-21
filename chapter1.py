#!/usr/bin/python3
from collections import Counter
from typing import List


def problem1(s: str) -> bool:
    """Implement an algorithm to determine if a string
    has all unique characters. What if you cannot use 
    additional data structures?
    """
    for c in s:
        if s.count(c) > 1:
            return False
    return True


def problem3(s1: str, s2: str) -> bool:
    """Give two strings, write a method to decide if one
    is a permutation of the other
    """
    if sorted(list(s1)) == sorted(list(s2)):
        return True
    return False


def problem4(s: str) -> str:
    """Write a method to replace all spaces in a string with '%20'
    """
    return s.replace(' ', '%20')


def problem5(s: str) -> str:
    """Implement a method to perform basic string compression using the counts
    of repeated characters. for example aabccccaaa -> a2b1c5a3
    """
    counter = Counter(s)
    count_string = ''
    for letter, count in counter.items():
        count_string += (letter + str(count))

    return count_string


def problem6(matrix: List[List]) -> List[List]:
    """Given an image represented by an NxN matrix, where each pixel in the image
    is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
    """
    columns = []
    N = len(matrix)
    for i in range(0, N):
        columns.append([row[i] for row in matrix])

    return columns


def problem7(matrix: List[List]) -> List[List]:
    """Write an algorithm such that if an element in an MxN matrix is 0, its
    entire row and column are set to 0
    """
    new_matrix = []
    N = len(matrix)
    M = len(matrix[0])
    print(f'N, M: {N}, {M}')
    rows = [False] * N
    cols = [False] * M
    print(len(rows))
    for i in range(0, N):
        for j in range(0, M):
            if matrix[i][j] == 0:
                rows[i] = True
                cols[j] = True
    for i in range(0, N):
        new_matrix.append([])
        for j in range(0, M):
            if rows[i] or cols[j]:
                new_matrix[i].append(0)
            else:
                new_matrix[i].append(matrix[i][j])

    return new_matrix


def is_substring(s1: str, s2: str) -> bool:
    if s2 in s1:
        return True
    return False


def problem8(s1: str, s2: str) -> bool:
    """Assume you have a method isSubstring which checks if one word is a substring
    of another. Given two strings, s1 and s2, write code to check if s2 is a rotation
    of s1 using only one call to isSubstring. (e.g. "lewaterbott" is a rotation of "waterbottle")
    """
    if len(s1) != len(s2):
        return False
    if not s1:
        return False
    return is_substring((s1+s1), s2)


if __name__ == "__main__":
    print(problem1('abc'))
    print(problem1('abccc'))
    print(problem3('abc', 'cba'))
    print(problem3('abccc', 'abc'))
    print(problem4('a b d d'))
    print(problem4('ab cc c'))
    print(problem5('aaaaaaabbddd'))
    print(problem6([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]))
    print(problem7([[1, 2, 3, 4], [5, 0, 6, 7], [8, 9, 10, 11]]))
    print(problem8('waterbdottle', 'lewaterbott'))


