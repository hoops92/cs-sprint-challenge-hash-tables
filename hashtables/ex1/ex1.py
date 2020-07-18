def get_indices_of_item_weights(weights, length, limit):
    """
    Finds two weights and adds the sum of weights to reach a weight limit.
    """
    # Your code here
    # Create a cache
    cache = {}

    # Run for each of the indexes in the list
    for idx in range(length):
        # How much until we reach the limit?
        remaining_weight = limit - weights[idx]

        # Have we seen already the remaining weight needed?
        # Look in the cache
        if remaining_weight in cache:
            # Create a tuple for the results
            result = (idx, cache[remaining_weight])
            # Return by descending weight
            result = sorted(result, reverse=True)
            return result
        else:
            # Add these weights in cache
            cache[weights[idx]] = idx

    return None
