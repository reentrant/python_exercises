def create_sorted_array_counters(array, m):
    counters = [0] * (m + 1)
    for e in array:
        counters[e] += 1
    return counters


def balancing_the_weight(array_a, array_b, m):
    """
    Problem: You are given an integer m (1 <= m <= 1 000 000) and two non-empty, zero-indexed
    arrays A and B of n integers, a0, a1, . . . , an−1 and b0, b1, . . . , bn−1 respectively
    (0 <= ai, bi <= m).
    The goal is to check whether there is a swap operation which can be performed on these
    arrays in such a way that the sum of elements in array A equals the sum of elements in
    array B after the swap. By swap operation we mean picking one element from array A and
    one element from array B and exchanging them.
    :param array_a:
    :param array_b:
    :param m:
    :return: boolean
    """
    result = False
    sum_a = sum(array_a)
    sum_b = sum(array_b)
    diff = sum_b - sum_a
    if diff % 2 == 1:
        return False
    diff //= 2
    counter_a = create_sorted_array_counters(array_a, m)

    for e in array_b:
        if 0 <= e - diff <= m and counter_a[e - diff]:
            return True
    return False


def sort_using_counters(array, m):
    result = [0] * len(array)
    counters = create_sorted_array_counters(array, m)
    index = 0
    for i, item in enumerate(counters):
        for _ in range(item):
            result[index] = i
            index += 1
    return result


def find_the_leader(array):
    n = len(array)
    size = 0
    for element in array:
        if size == 0:
            size += 1
            value = element
        else:
            if value != element:
                size -= 1
            else:
                size += 1
    candidate = -1
    if size > 0:
        candidate = value
    leader = -1
    count = 0
    for item in array:
        if item == candidate:
            count += 1
    if count > n // 2:
        leader = candidate
    return leader


if __name__ == '__main__':
    # print(balancing_the_weight([1, 1, 2], [3, 2, 1], 5))
    # print(create_sorted_array_counters([0, 0, 4, 2, 4, 5], 5))
    # print(sort_using_counters([1, 9, 9, 4, 8, 8, 6], 10))
    print(find_the_leader([6, 8, 4, 6, 8, 6, 6]))
