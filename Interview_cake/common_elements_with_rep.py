def find_duplicates(a, b):
    """
    Given 2 different lists of integers,
    write a function that will return their intersection.

    Example:

    [1,2,2,3] and [2,2,3,4] should intersect as [2,2,3] and not just [2,3].
    :param a:
    :param b:
    :return:
    """
    #     items = {}
    #     for e in a:
    #         if e in items:
    #             items[e] += 1
    #         else:
    #             items[e] = 1
    #     for e in b:
    #         if e in items and items[e] > 0:
    #             common.append(e)
    #             items[e] -= 1
    common = []
    if len(b) and len(a):
        reference = b[:]
        for i in range(len(a)):
            if a[i] in reference:
                common.append(reference.pop(reference.index(a[i])))
            if reference:
                continue
            else:
                break
    return common


if __name__ == '__main__':
    lst_1 = [1, 2, 2, 3]
    lst_2 = [2, 2, 3, 4]
    print(find_duplicates(lst_1, lst_2))
    lst_1 = [1, 2, 2, 3]
    lst_2 = []
    print(find_duplicates(lst_1, lst_2))
    lst_1 = []
    lst_2 = [2, 2, 3, 4]
    print(find_duplicates(lst_1, lst_2))
