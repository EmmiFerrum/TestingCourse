import pytest


def test_set_one(fixture_create_set, fixture_create_set_cute):
        #print (Cute_animals.difference(fixture_create_set))
    assert fixture_create_set_cute.difference(fixture_create_set) == {'kenguru', 'turtle'} # Проверка на поиск отличий в двух множествах


def test_set_two (fixture_create_set):
    print ( "\n", len(fixture_create_set))
    assert len(fixture_create_set) != 8 # Проверка на количество элементов. в множестве написано 8, но 2 из них повторяются, поэтому уникальных элементов 6 !=8


def test_set_three(fixture_create_set, fixture_create_set_cute):
    fixture_create_set.difference_update(fixture_create_set_cute)
    print('\n', fixture_create_set)
    assert fixture_create_set == {'lama', 'pig', 'cow', 'elephant'} # Проверка на удаление повторяющихся элементов в множествах


@pytest.mark.parametrize("numbers", { 1, 2, 3})
def test_set_four (fixture_create_set, fixture_create_set_cute, numbers):
    fixture_create_set.add(numbers)
    print(fixture_create_set)
    assert len(fixture_create_set) == 7

def test_set_five (fixture_create_set,fixture_create_set_cute):
    fixture_create_set_cute.discard('kenguru')
    fixture_create_set_cute.discard('turtle')
    print (fixture_create_set_cute)
    assert fixture_create_set_cute.issubset(fixture_create_set) # проверка на то, что после удаления лишних элементов из 2го множества, все элементы 2го множества присутствуют в 1ом



