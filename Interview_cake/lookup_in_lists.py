
def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: ixs_tuple: (a tuple of 2 ints) The indices of the two elements whose sum is equal to
    target_sum. If there are no two numbers, the function should return None. For example,
    find_two_sum([3, 1, 5, 7, 5, 9], 10)
    should return a single tuple containing any of the following pairs of indices:
    0 and 3 (or 3 and 0) as 3 + 7 = 10
    """

    calculated = {}

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if j == i or (j, i) in calculated:
                continue
            result = numbers[i] + numbers[j]
            aux_tuple = (i, j)
            if result == target_sum:
                return aux_tuple
            calculated[aux_tuple] = result
            # print(calculated)
    return None


if __name__ == '__main__':
    print(find_two_sum([3, 1, 5, 7, 5, 9], 10))

