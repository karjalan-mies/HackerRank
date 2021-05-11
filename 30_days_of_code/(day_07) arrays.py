#!/bin/python3

import math
import os
import random
import re
import sys


def get_string(arr):
    string_from_list = ''
    if len(arr) == n:
        for i in range(1, n + 1):
            if 1 <= arr[i*(-1)] <= 10000:
                string_from_list = string_from_list + ' ' + str(arr[i*(-1)])
            else:
                return None
        return string_from_list.strip()
    else:
        return None


if __name__ == '__main__':
    n = int(input().strip())
    if 1 <= n <=1000:
        arr = list(map(int, input().rstrip().split()))
        string_from_list = get_string(arr)
        if string_from_list:
            print(string_from_list)
