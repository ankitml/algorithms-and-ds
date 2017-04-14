def binary_search(array, element):
    return _binary_search(array, element, 0, len(array))

def _binary_search(array, element, start, last):
    mid = (start + last) // 2
    if array[mid] == element:
        return mid
    if array[mid] > element:
        last = mid
    if array[mid] < element:
        start = mid
    return _binary_search(array, element, start, last)


def maxmin(l):
    ll = l.copy()
    n = ll.pop()
    return _maxmin(ll, n, n)

def _maxmin(l, big, small):
    element = l.pop

