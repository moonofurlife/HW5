from test2 import logger


@logger('log_3.log')
def FlatIteratorWithDecorator(values_list):
    res = (value for list_ in values_list for value in list_)
    while True:
        try:
            yield next(res)
        except StopIteration:
            break


values_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

if __name__ == "__main__":
    print('Задание 1')
    print(list(FlatIteratorWithDecorator(values_list)))

