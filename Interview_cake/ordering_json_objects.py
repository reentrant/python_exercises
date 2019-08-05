def swap(array, a, b):
    aux = array[a]
    array[a] = array[b]
    array[b] = aux


def sort_criteria(py_dict):
    return py_dict['price']


def sort_by_price_ascending(json_string):
    temp_list = []

    # FIRST TRY:
    for e in eval(json_string):
        temp_list.append(e)
    # print(temp_list)
    # SECOND TRY:
    index = 0
    while index < len(temp_list) -1:
        smaller = 1000000000
        smaller_ix = 1
        for i in range(1, len(temp_list)):
            if temp_list[i].get('price') < smaller:
                smaller = temp_list[i].get('price')
                smaller_ix = i
        if temp_list[index].get('price') > smaller:
            swap(temp_list, index, smaller_ix)
        # print(temp_list)
        index += 1
    return temp_list


if __name__ == '__main__':
    results = sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]')
    print(results)
    #sorted(obj_dict.items(), key = lambda pair: pair[1], reverse = True )
