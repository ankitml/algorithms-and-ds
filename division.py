import time

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print('%r (%r, %r) %2.4f sec' % \
              (method.__name__, args, kw, te-ts))
        return result
    return timed


def div(a, b):
    """
    a/b without using division operator
    """

    if b > a:
        return 0
    if b == a:
        return 1
    return 1 + div(a - b, b)


def div_fast(a, b):
    """
    a/b without using division operator
    """

    if b > a:
        return 0
    if b == a:
        return 1

    # assuming a%b = 0
    # the answer is between 1 and a, do the binary search of
    small = 1
    large = a
    while True:
        mid = int((large + small)/2)
        trial = mid * b
        if trial == a:
            return mid
        if trial > a:
            large = mid
        else:
            small = mid


def merge_sorted_lists(a, b):
    a_index, b_index = 0, 0
    merged_list = []
    for i in range(0, len(a) + len(b)):
        try:
            a_position = a[a_index]
        except IndexError:
            retur
        if a[a_index] <= b[b_index]:
            merged_list.append(a[a_index])
            a_index +=1
        else:
            merged_list.append(b[b_index])
            b_index += 1

    return merged_list

def binary_search(l, element, start=None, end=None):
    if not end:
        end = len(l)
    if not start:
        start = 0

    mid = int((end + start) / 2)
    print(mid)

    if l[mid] == element:
        return mid

    if l[mid] > element:
        return binary_search(l, element, start, mid-1)

    if l[mid] < element:
        return binary_search(l, element, mid+1, end)


    pivot = l[mid]
    lesser


from collections import deque

def bfs(graph, centre, element, to_search=None, already_searched=None):
    if not to_search:
        to_search = deque()
        already_searched = []

    for e in graph[centre]:
        if e not in already_searched:
            to_search.append(e)

    for e in to_search:
        if e == element:
            already_searched.append(e)
            return element


@timeit
def start(n):
    print(reach_one(n))



def reach_one(n):
    if n == 1:
        return 0
    if n in [2,3]:
        return 1

    possible_set = set([reach_one(n-1)])
    if n%2 ==0:
        possible_set.add(reach_one(n/2))

    if n%3 == 0:
        possible_set.add(reach_one(n/3))

    return 1 + min(possible_set)


def karatsuba_two(a, b):
    print(a, b)
    if (a // 10) == 0 and (b//10) == 0:
        return a * b

    i,k = a // 10, b // 10
    j, l = a % 10, b % 10

    A = karatsuba_two(i, k)
    B = karatsuba_two(j, l)
    C = karatsuba_two(i + j,  k + l) - A - B
    return 100*A + B + 10*C

    










