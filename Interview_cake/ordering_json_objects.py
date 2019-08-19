def swap(array, a, b):
    array[a], array[b] = array[b], array[a]
    return array


def sort_by_price(py_dict):
    return py_dict.get('price')


def sort_by_price_ascending(json_string):
    py_list = eval(json_string)
    return sorted(py_list, key=sort_by_price)


if __name__ == '__main__':
    results = sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]')
    print(results)
    print(swap([1, 2, 3, 4, 5], 0, 1))
