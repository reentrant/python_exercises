def create_prefix_sums(array):
    """
    Given an array of n elements, we have the sums of consecutive elements:
            a0,     a1,        ...,        an-1
    p0=0  p1=a0   p2=a0 + a1               pn=a0 + a1 + ... + an-1
    :param array:
    :return:
    """
    prefix_sums = [0]
    for i in range(1, len(array) + 1):
        prefix_sums.append(prefix_sums[i - 1] + array[i - 1])
    return prefix_sums


def calculate_slice(prefix_array, start, end):
    return prefix_array[end + 1] - prefix_array[start]


def calculate_slice_sums(array, k, m):
    """
    Problem: You are given a non-empty, zero-indexed array A of n (1 <= n <= 100 000) integers
    a0, a1, . . . , an−1 (0 <= ai <= 1 000).
    :param array:
    :param k: You are also given integers k and m (0 <= k,m < n).
    :param m:
    :return:
    """
    n = len(array)
    result = 0
    pref = create_prefix_sums(array)
    # slice from k to m or from m to k:
    for p in range(min(m, k) + 1):
        left_pos = k - p
        right_pos = min(n - 1, max(k, k + m - 2 * p))
        result = max(result, calculate_slice(pref, left_pos, right_pos))
        print(left_pos, right_pos, result)
    for p in range(min(m + 1, n - k)):
        right_pos = k + p
        left_pos = max(0, min(k, k - (m - 2 * p)))
        result = max(result, calculate_slice(pref, left_pos, right_pos))
        print(left_pos, right_pos, result)
    return result


if __name__ == '__main__':
    sums = create_prefix_sums([2, 3, 7, 5, 1, 3, 9])
    print(sums)
    print(calculate_slice_sums([2, 3, 7, 5, 1, 3, 9], 4, 6))
