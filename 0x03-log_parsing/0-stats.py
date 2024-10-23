#!/usr/bin/python3
"""Log parsing"""
import sys
import re
from typing import Dict


def print_stats(status_codes: Dict, file_size: int):
    """ function that reads stdin line by line and computes metrics
    Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" 
    <status code> <file size> (if the format is not this one, 
    the line must be skipped)

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
        counter += 1
        data = line.split()
        if len(data) > 2:
            total_file_size += int(data[-1])
            code = data[-2]
            if code in status_codes:
                status_codes[code] += 1
        if counter % 10 == 0:
            print_stats(status_codes, total_file_size)
except KeyboardInterrupt:
    print_stats(status_codes, total_file_size)
    raise KeyboardInterrupt
