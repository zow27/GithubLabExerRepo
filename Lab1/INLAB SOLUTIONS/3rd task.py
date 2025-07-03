def our_sum(lower, upper, margin=0):
    indent = ' ' * margin
    print(indent, lower, upper)
    if lower > upper:
        print(indent, 0)
        return 0
    result = lower + our_sum(lower + 1, upper, margin + 4)
    print(indent, result)
    return result
