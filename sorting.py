#!/usr/bin/python3
import sys
from typing import List, Tuple


def swap_spots_in_array(values: List[int], first_index: int, second_index: int) -> List[int]:
    new_list = values[:first_index] + [values[second_index]] + values[first_index+1:second_index] + [values[first_index]] + values[second_index+1:]
    return new_list


def insert_value_in_array(values: List[int], new_index: int, old_index: int) -> List[int]:
    new_list = values[:new_index] + [values[old_index]] + values[new_index:old_index] + values[old_index+1:]
    return new_list


def insertion_sort(values: List[int]) -> List[int]:
    for i in range(len(values)):
        first = values[i]
        for j in range(i+1, len(values)):
            nxt = values[j]
            if nxt < first:
                values = swap_spots_in_array(values, i, j)
    return values


def selection_sort(values: List[int]) -> List[int]:
    for i in range(len(values)):
        current_min = None
        for j in range(i, len(values)):
            if not current_min or values[j] < values[current_min]:
                current_min = j
        values = insert_value_in_array(values, i, current_min)
        print(f'v: {values}')

    return values


def bubble_sort(values: List[int]) -> List[int]:
    swaps = True
    while swaps:
        swaps = False
        for i in range(len(values) - 1):
            left_val = values[i]
            right_val = values[i+1]
            if left_val > right_val:
                values[i] = right_val
                values[i+1] = left_val
                swaps = True
    return values


def merge(values1: List[int], values2: List[int]) -> List[int]:
    i = j = 0
    new_values = []
    while i < len(values1) or j < len(values2):
        if i == len(values1):
            left = sys.maxsize
        else:
            left = values1[i]
        if j == len(values2):
            right = sys.maxsize
        else:
            right = values2[j]

        if left < right:
            new_values.append(left)
            i += 1
        else:
            new_values.append(right)
            j += 1
    return new_values


def merge_sort(values: List[int]) -> List[int]:
    if len(values) == 1:
        return values
    if len(values) == 2:
        if values[0] < values[1]:
            return values
        else:
            return [values[1], values[0]]
    mid_point = int(len(values) / 2)
    half1 = values[:mid_point]
    half2 = values[mid_point:]
    sorted_half1 = merge_sort(half1)
    sorted_half2 = merge_sort(half2)
    return merge(sorted_half1, sorted_half2)


def find_first_bigger(values: List[int], pivot: int) -> int:
    item_from_left = None
    for i in range(len(values)):
        item_from_left = i
        if values[i] > pivot:
            return i
    return item_from_left


def find_first_smaller(values: List[int], pivot: int) -> int:
    item_from_right = None
    for j in reversed(range(len(values) - 1)):
        item_from_right = j
        if values[j] < pivot:
            # print(f'smaller right{j}')
            return j
    return item_from_right


def partition(values: List[int]) -> Tuple[int, List[int]]:
    print(f'v1: {values}')
    if len(values) == 1:
        return 0, values
    pivot_index = len(values) - 1

    pivot = values[pivot_index]

    item_from_left = find_first_bigger(values, pivot)
    item_from_right = find_first_smaller(values, pivot)

    while item_from_left < item_from_right:
        print(f"left: {item_from_left}, right: {item_from_right}")
        values = swap_spots_in_array(values, item_from_left, item_from_right)
        item_from_left = find_first_bigger(values, pivot)
        item_from_right = find_first_smaller(values, pivot)
    values = swap_spots_in_array(values, item_from_left, pivot_index)

    return item_from_left, values


def quick_sort(values: List[int]) -> List[int]:
    if values:
        pivot_index, values = partition(values)
        values[:pivot_index] = quick_sort(values[:pivot_index])
        values[pivot_index + 1:] = quick_sort(values[pivot_index + 1:])

    return values


if __name__ == "__main__":
    values = [2, 5, 1, 3, 6, 4]
    print(insertion_sort(values))
    print(selection_sort(values))
    print(bubble_sort(values))
    print(merge_sort([1, 3, 5, 2, 4, 6, 9, 10]))
    print(quick_sort(values))






