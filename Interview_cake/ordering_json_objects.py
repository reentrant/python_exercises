def sort_by_price_ascending(json_string):
    result = []

    for e in eval(json_string):
        prod_dict = {}
        for k, v in e.items():
            prod_dict[k] = v
        result.append(prod_dict)

    sorted(result, key=lambda pair: pair['price'], reverse=True)
    return result

print(sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'))


    #sorted(obj_dict.items(), key = lambda pair: pair[1], reverse = True )
