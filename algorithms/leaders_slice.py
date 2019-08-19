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


def create_sorted_array_counters(counters, array, start, end):
    for i in range(start, end):
        counters[array[i]] += 1
    # print(counters)


def solution(k, m, array):
    """
    N and M are integers within the range [1..100,000];
    K is an integer within the range [1..N];
    each element of array A is an integer within the range [1..M].
    :param k:
    :param m:
    :param array:
    :return:
    """
    leaders = set()
    half = len(array) / 2

    for i in range(len(array) - k + 1):
        counters = [0] * (m + 2)
        before = array[:i]
        print(f"{before} ", end='')
        if i - 0:
            create_sorted_array_counters(counters, array, 0, i)

        segment = []
        for j in range(i, i + k):
            segment.append(1 + array[j])
        print(f"{segment}", end='')
        if k:
            create_sorted_array_counters(counters, segment, 0, k)

        after = array[i+k:]
        print(f"{after}")
        if len(array) - i - k:
            create_sorted_array_counters(counters, array, i + k, len(array))

        if max(counters) > half:
            leaders.add(counters.index(max(counters)))
        print(counters, leaders)
        # breakpoint()
    return sorted(list(leaders))


if __name__ == '__main__':
    print(solution(4, 2, [1, 2, 2, 1, 2]))
    # print(solution(3, 5, [2, 1, 3, 1, 2, 2, 3]))
    # print(solution(1, 1, [1]))
