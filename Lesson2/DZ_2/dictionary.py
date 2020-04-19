import pytest


def test_dict_one(fixture_mau):
    fixture_mau.get('month')
    if fixture_mau.get('month') == 1:
        fixture_mau['month'] = 'January'
    elif fixture_mau.get('month') == 2:
        fixture_mau['month'] = 'February'
    elif fixture_mau.get('month') == 3:
        fixture_mau['month'] = 'Mart'
    elif fixture_mau.get('month') == 4:
        fixture_mau['month'] = 'April'
    elif fixture_mau.get('month') == 5:
        fixture_mau['month'] = 'May'
    elif fixture_mau.get('month') == 6:
        fixture_mau['month'] = 'June'
    elif fixture_mau.get('month') == 7:
        fixture_mau['month'] = 'July'
    elif fixture_mau.get('month') == 8:
        fixture_mau['month'] = 'August'
    elif fixture_mau.get('month') == 9:
        fixture_mau['month'] = 'September'
    elif fixture_mau.get('month') == 10:
        fixture_mau['month'] = 'October'
    elif fixture_mau.get('month') == 11:
        fixture_mau['month'] = 'November'
    elif fixture_mau.get('month') == 12:
        fixture_mau['month'] = 'December'

    else:
        print('cat')

    print('\n', fixture_mau)

    assert fixture_mau.get('month') == 'December'  # Проверка на попадание числа на декабрь


def test_dict_two(fixture_mau):
    print (fixture_mau)
    fixture_mau.clear()
    print (fixture_mau)
    assert len(fixture_mau) == 0  # Проверка на очищение словаря


def test_dict_three (fixture_mau):
    fixture_mau ['year'] = 2020
    print(fixture_mau)
    assert 2020 in fixture_mau.values()  # Проверка на то, что значение года изменено и теперь присутствует в словаре


@pytest.mark.parametrize("asd", [1,2,3,4])

def test_dict_four (fixture_mau, asd):
    print(fixture_mau)
    fixture_mau ['month'] = asd
    print(fixture_mau)
    assert asd in fixture_mau.values()  # Проверка на замену значения на значение из параметров параметризации теста


def test_dict_five (fixture_mau):
    fixture_mau ['century'] = 20
    print('\n', fixture_mau)
    assert 'century' in fixture_mau  # проверка на добавление нового элемента словаря