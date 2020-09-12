def intersection(arrays):
    """
    Find intersection between different lists of integers
    """
    # Create a cache to save "seen" integers
    cache = {}
    # Your code here
    # Get the total # of lists to look through
    num_list = len(arrays)

    # Create a lsit to save the intersection values
    result = []

    # Create a for loop to go through each list
    for lst in arrays:
        # Loop through each item in list
        for item in lst:
            # Add the items in cache as keys if not there
            # Count in how many lists have items present as values
            if item not in cache:
                cache[item] = 1
            else:
                # Ff the element in already in the cache
                # Increment its value by 1
                cache[item] += 1
                # Did the item count reach the total number of lists?
                # If yes, add the number in the result list
                if cache[item] == num_list:
                    result.append(item)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
