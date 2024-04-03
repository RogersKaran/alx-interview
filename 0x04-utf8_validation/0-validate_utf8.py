def validUTF8(data):
    num_bytes = 0
    for byte in data:
        if num_bytes == 0:
            if byte >> 7 == 0:
                continue  # Single byte character
            elif byte >> 5 == 0b110:
                num_bytes = 1  # Two-byte character
            elif byte >> 4 == 0b1110:
                num_bytes = 2  # Three-byte character
            elif byte >> 3 == 0b11110:
                num_bytes = 3  # Four-byte character
            else:
                return False  # Invalid UTF-8 encoding
        else:
            if byte >> 6 != 0b10:
                return False  # Invalid UTF-8 encoding
            num_bytes -= 1
    return num_bytes == 0  # True if all characters have been validated

