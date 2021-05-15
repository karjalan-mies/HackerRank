#!/bin/python3

import math
import os
import random
import re
import sys


def convert_to_binary_from_decimal(n):
    binary_numbers = ''
    while n > 0:
        binary_numbers = str(n % 2) + binary_numbers
        n = n // 2
    return binary_numbers


def find_maximum_ones(binary_numbers):
    max_ones_count = 0
    current_ones_count = 0
    for number in binary_numbers:
        if int(number):
            current_ones_count += 1
        else:
            if current_ones_count > max_ones_count:
                max_ones_count = current_ones_count
            current_ones_count = 0
        if current_ones_count > max_ones_count:
            max_ones_count = current_ones_count
    return max_ones_count

if __name__ == '__main__':
    n = int(input().strip())
    if 1 <= n <= 10**6:
        binary_numbers = convert_to_binary_from_decimal(n)
        max_ones_count = find_maximum_ones(binary_numbers)
        print(binary_numbers)
        print(max_ones_count)
