import pytest


def test_list_one(fixture_create_list):
    assert len(fixture_create_list) == 4 #проверка количества элементов


def test_list_two(fixture_create_list): #проверка на добавление элемента
    fixture_create_list.append('watermelon')
    assert len(fixture_create_list) == 5


def test_list_three(fixture_create_list): #проверяет наличие элемента в списке
    assert 'apple' in fixture_create_list


@pytest.mark.parametrize('colors', ['white', 'red', 'blue', 'yellow']) #к списку добавляется по 1 из парамметров, выходит 4 теста
def test_list_four(fixture_create_list, colors):
    fixture_create_list.append(colors)
    print(fixture_create_list)
    assert 'blue' in fixture_create_list #проверка, что в список добавленно конкретное значение. из 4х тестов 1 - будет успешный.


def test_list_five(fixture_create_list): #Проверка на удаление элемента
    fixture_create_list.remove('apple')
    assert 'apple' not in fixture_create_list

