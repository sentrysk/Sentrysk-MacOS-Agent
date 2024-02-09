#!/usr/bin/env python3

# Libraries
##############################################################################
import math
##############################################################################

# Functions
##############################################################################
def convert_size(size_bytes):
    """
    Convert the size in bytes to a more human-readable format.
    """
    if size_bytes == 0:
        return "0B"
    size_names = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
    i = int(math.log(size_bytes, 1024))
    size = round(size_bytes / (1024 ** i), 2)
    return f"{size} {size_names[i]}"
##############################################################################