#!/usr/bin/python3
"""
Module for UTF-8 Validation
"""


def validUTF8(data):
    """
    Method that determines if a given data set represents a valid UTF-8 encoding
    """

    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Mask to check if the most significant bit is set
    mask1 = 1 << 7

    # Mask to check if the second most significant bit is set
    mask2 = 1 << 6

    # Iterate through the data set
    for num in data:

        # Get the bit representation
        mask_num = 1 << 7
        while num & mask_num:
            num_bytes += 1
            mask_num = mask_num >> 1

        # If the current data is not a valid UTF-8 character
        if num_bytes == 0:
            continue

        # If the current data is a part of a UTF-8 character
        if num_bytes == 1 or num_bytes > 4:
            return False

        # Decrement the number of bytes
        num_bytes -= 1

    # If there are no bytes left
    return num_bytes == 0
