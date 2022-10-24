from functions.increase_by_percentage import increase_by_percent
from functions.increase_by_amount import increase_by_amount


def interate_list(input_list: list):
    for i in range(len(input_list)):
        print(f"{i+1}: {input_list[i]}", end=' ')


print('list - 1')
interate_list(increase_by_percent(20_000, 5))
print('\n')
print('list - 2')
interate_list(increase_by_amount(25_000, 500))
