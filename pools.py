import concurrent.futures as cf
import multiprocessing as mp
import numpy as np


def how_many_within_range(row, minimum=4, maximum=8):
    """Returns how many numbers lie within `maximum` and `minimum` in a given `row`"""
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count


def main():
    # Prepare data
    np.random.RandomState(100)
    arr = np.random.randint(0, 10, size=[200000, 5])
    data = arr.tolist()
    # Run
    pool_starmap(data)
    pool_map(data)
    futures_pool(data)


def pool_map(data):
    with mp.Pool() as pool:
        # Only one arg is passed to fn for each element in list (iterable),
        # the other two fn args are defaulted
        results = pool.map(how_many_within_range, [row for row in data])
    print(results[:20])


def pool_starmap(data):
    pool = mp.Pool(mp.cpu_count())
    # second arg in starmap is a list comp that stuffs defaults into
    # tuple (iterable), passed to fn as args
    results = pool.starmap(how_many_within_range, [(row, 4, 8) for row in data])
    pool.close()
    print(results[:20])

def futures_pool(data):
    with cf.ProcessPoolExecutor() as executor:
        results = executor.map(how_many_within_range, [row for row in data])
    print(results[:20])


if __name__ == "__main__":
    main()
