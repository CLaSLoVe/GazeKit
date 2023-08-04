def encode_bool_lists(bool_lists):
    """
    Encode multiple boolean lists into an integer list.
    :param bool_lists: A 2D list containing multiple boolean lists.
    :return: The encoded integer list.
    """
    res = []
    n_bits = len(bool_lists[0])

    for bool_list in bool_lists:
        bin_int = 0
        mask = 1 << (n_bits - 1)

        for bit in bool_list:
            if bit:
                bin_int |= mask
            mask >>= 1

        res.append(bin_int)

    return res


def decode_bool_list(encoded_int, n_bits):
    """
    Decode an integer into a boolean list.
    :param encoded_int: The encoded integer.
    :param n_bits: The number of bits in the boolean list.
    :return: The decoded boolean list.
    """
    bool_list = []
    mask = 1 << (n_bits - 1)

    for _ in range(n_bits):
        bit = (encoded_int & mask) != 0
        bool_list.append(bit)
        mask >>= 1

    return bool_list

