from log_utils import logger
from log_utils import logger_with_path_fabric
from netology_py_advanced_iterator import flat_generator
from netology_py_advanced_iterator import flat_generator_fixed
from netology_py_advanced_iterator import my_list
from netology_py_advanced_iterator import my_nested_list


# Задача 1:
@logger
def summation(*args):
    return sum(args)


# Задача 2:
# В переменной path лежит желаемый путь до файла с логами.
path = 'logs'


@logger_with_path_fabric(path)
def summation_2(*args):
    return sum(args)

# Реализация задачи 3 в netology_py_advanced_iterator.py.


if __name__ == '__main__':
    # Очищение логов перед новым запуском программы.
    open('log.txt', 'w').close()
    open(F'{path}/log.txt', 'w').close()
    # Вызов функций для демонстрации работы декораторов.
    print(summation(5, 6))
    print('_'*100)
    print(summation_2(5, 6))
    print('_'*100)
    for i in flat_generator_fixed(my_list):
        print(i)
    print('_'*100)
    for i in flat_generator(my_nested_list):
        print(i)
