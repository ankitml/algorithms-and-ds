def combine_sorted(a, b):
    """
    Combines two sorted lists into another sorted list
    O(n)
    """
    c = []
    index_a, index_b = 0,0
    max_index_a, max_index_b = len(a), len(b)
    while True:
        if a[index_a] < b[index_b]:
            c.append(a[index_a])
            index_a += 1
        else:
            c.append(b[index_b])
            index_b += 1
        if index_b == max_index_b:
            c.extend(a[index_a:])
            break
        if index_a == max_index_a:
            c.extend(b[index_b:])
            break
    return c

def combine_sorted2(a, b):
    """
    Combines two sorted lists into another sorted list
    O(n)
    """
    c = []
    while True:
        if a[0] < b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))
        if len(a) == 0:
            c.extend(b)
            break
        if len(b) == 0:
            c.extend(a)
            break
    return c

def sort(l):
    return _sort(l)

def _sort(l):
    if len(l) <= 1:
        return l
    else:
        mid = len(l) // 2
        first = l[0:mid]
        second = l[mid:]
        return combine_sorted2(_sort(first), _sort(second))
