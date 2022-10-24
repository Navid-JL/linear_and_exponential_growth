def increase_by_factor(initial_value, increase_factor):
    some_list = []

    some_list.append(initial_value)

    for i in range(1, 12):
        initial_value = initial_value * increase_factor
        some_list.append(int(initial_value))

    return some_list
