def increase_by_percent(initial_value, increase_percentage):
    some_list = []

    some_list.append(initial_value)

    for i in range(1, 12):
        some_list.append(int(initial_value*((increase_percentage/100) + 1)**i))

    return some_list
