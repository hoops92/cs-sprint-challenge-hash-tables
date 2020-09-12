def has_negatives(a):
    """
    Negative numbers
    """
    # Code here
    # Create a list and cache to save negative values
    result = []
    my_dict = {}

    # Create a For loop to go through the list
    for x in a:
        my_dict[x] = x
        # If # in is not 0 or in the cache
        if x != 0 and -x in my_dict:
            # Returns # as a positive
            result.append(abs(x))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
