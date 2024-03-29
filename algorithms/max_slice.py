def golden_max_slice(array):
    sums = max_slice = 0
    for sub_array in array:
        sums = max(0, sums + sub_array)
        max_slice = max(max_slice, sums)
        print(sub_array, sums, max_slice)
    return max_slice


if __name__ == '__main__':
    print(golden_max_slice([5, -7, 3, 5, -2, 4, -1]))
