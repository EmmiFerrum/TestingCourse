import pytest


def test_string_one(fixture_create_list):
    a = ''.join(fixture_create_list)
    print(a)
    assert a.isalpha()  # Проверка, что строка, которую мы преобразовали из списка содержит только буквы


def test_string_two (fixture_create_list):
    a = ''.join(fixture_create_list)
    b = a.center(len(a)+2)  # Прибавляем пробелы в начало и в конец строки
    assert len(a) < len(b)  # Проверка, что пробелы добавились


def test_string_three ():
    a = 'Hello World'
    b = a.upper()
    print (b)
    assert b.isupper()


@pytest.mark.parametrize ('punctuation', ['!', '.', '?'])
def test_string_four(punctuation):
    a = 'Hello World'
    b = a + punctuation
    print(b)
    assert len(b) == len(a)+1


def test_string_five():
    a = 'abcdefghijklmnopq'
    assert a[2] == 'c'  # Проверяем, что 3й по индеусу знак это с
