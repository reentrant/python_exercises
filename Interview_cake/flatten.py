# Write some code, that will flatten an array of arbitrarily nested arrays of integers into a
# flat array of integers. e.g. [[1,2,[3]],4] -> [1,2,3,4].

def flat_a_list(nested_list):
    flatten_list = []

    for element in nested_list:
        if isinstance(element, list):
            flatten_list += flat_a_list(element)
        else:
            flatten_list.append(element)
    return flatten_list


if __name__ == '__main__':
    print(flat_a_list([[1,2,[3]],4]))
