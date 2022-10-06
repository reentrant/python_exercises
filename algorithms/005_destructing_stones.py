def lastStoneWeight(weights):
    # Write your code here
    weights = sorted(weights, reverse=True)
    while len(weights) > 1:
        print(weights)
        new_value = weights[0] - weights[1]
        weights.pop(0)
        weights.pop(0)
        if new_value:
            weights.append(new_value)
        weights = sorted(weights, reverse=True)
    if weights:
        return weights[0]
    else:
        return 0

if __name__ == '__main__':
    print(lastStoneWeight([2, 4, 5]))
    print(lastStoneWeight([1, 2, 3, 6, 7, 7]))

