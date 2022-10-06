class Test:
    def __init__(self):
        self.prop = True


def validate_swaps(lst, _string):
    results = []
    lst = [list(i) for i in lst]
    _string = list(_string)
    for word in lst:
        valid = False
        for i in range(0, len(word)):
            for j in range(i + 1, len(word)):
                new = word.copy()
                new[i] = word[j]
                new[j] = word[i]
                # print(i, j, new, _string)
                if new == _string:
                    valid = True
        results.append(valid)
    return results


if __name__ == '__main__':
    print(validate_swaps(["BACDE", "EBCDA"], "ABCDE"))
    a = Test()
    b = a
    print(a is b)
    print(id(a))
    print(id(b))
