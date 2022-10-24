def increase_by_amount(initial_value, increase_amount):
    some_list = []

    some_list.append(initial_value)

    for i in range(1, 12):
        initial_value += increase_amount
        some_list.append(int(initial_value))

    return some_list
