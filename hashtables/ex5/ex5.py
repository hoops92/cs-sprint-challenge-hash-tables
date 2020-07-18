



def finder(files, queries):
    """
    Given a list of full paths to files, and a list of filenames to query,
    report all the full paths that match that filename.
    """
    # Your code here
    # Create a cache where the last part is the key, path of /bin/foo would have the key foo
    cache = {k.split('/')[-1]: [] for k in files}
    result = []

    # For loop that goes over all the paths and adds them to the full path to the key that matches to the last part of the path
    for f in files:
        f_type = f.split('/')[-1]
        cache[f_type].append(f)

    # A cache with all possible last file paths and all paths that apply to that last part
    # For loop thru our queries and if the query is in the cache, it adds the values of that key to our 
    # result list
    for q in queries:
        if q in cache:
            result += cache[q]

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
