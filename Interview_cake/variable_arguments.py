def pipeline(*funcs):
    """
    The method should accept a variable number of functions, and it should return a new function
    that accepts one parameter arg.

    The returned function should call the first function in the pipeline with the parameter arg,
    and call the second function with the result of the first function.
    The returned function should continue calling each function in the pipeline in order,
    following the same pattern, and return the value from the last function.
    :param funcs:
    :return:
    """
    def helper(arg):
        for fun in funcs:
            arg = fun(arg)
        return arg

    return helper


if __name__ == '__main__':
    fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
    print(fun)
    print(fun(3))  # should print 5.0
