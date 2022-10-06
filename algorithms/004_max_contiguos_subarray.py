def maximumSum(arr):
    # Write your code here
    sums = max_slice = 0
    for sub_array in arr:
        sums = max(0, sums + sub_array)
        max_slice = max(max_slice, sums)
        print(sub_array, sums, max_slice)
    return max_slice


if __name__ == "__main__":
    print(maximumSum([-1, -2, 3, 4]))
