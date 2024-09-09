import numpy as np

def partition(a: np.ndarray, low: int, high: int):

    pivot = a[high]

    i = low

    for j in range(low, high):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1

        a[i], a[high], = a[high], a[i]
    return i


def mQuicksort(a: np.ndarray, low: int, high: int, med):
    pi = partition(a, low, high)

    if (pi - low == med - 1):
        return a[pi]
    if (pi - low > med - 1):
        return mQuicksort(a, low, pi - 1, med)

    return mQuicksort(a, pi + 1, high, med - pi + low - 1)


arr = np.array([12, 3, 6, 2, 19, 5, 9, 11])

m = int(arr.size) // 2


print(mQuicksort(arr, 0, int(arr.size) - 1, int(arr.size-m)))


