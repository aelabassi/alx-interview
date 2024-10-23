#!/usr/bin/python3
"""Log parsing"""
import sys
import re
from typing import Dict


def print_stats(status_codes: Dict[str, int], file_size: int):
    """ function that reads stdin line by line and computes metrics
    Args:
        status_codes (dict): dictionary with status codes
        file_size (int): file size
    Returns:
        None
        """
    print("File size: {}".format(file_size))
    for key, value in sorted(status_codes.items()):
        print("{}: {}".format(key, value))


total_file_size = 0
counter = 0
code = 0
status_codes = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
}
try:
    for line in sys.stdin:
        s_line = line.split()
        rs_line = s_line[::-1]
        if len(rs_line) > 2:
            counter += 1

            if counter <= 10:
                total_file_size += int(rs_line[0])
                code = rs_line[1]

                if code in status_codes.keys():
                    status_codes[code] += 1
        if counter % 10 == 0:
            print_stats(status_codes, total_file_size)
            counter = 0
finally:
    print_stats(status_codes, total_file_size)
