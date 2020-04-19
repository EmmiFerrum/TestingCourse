import pytest

# Fixtures
@pytest.fixture()
def first_fixture():
    print('first fixture - done')

@pytest.fixture()
def second_fixture():
    print('second fixture - done')

def test_1 (first_fixture):
    pass

def test_2 (fixture_out_1):
    pass

def test_3_number (fixture_return_rnd_number):
    assert fixture_return_rnd_number == 3

#Фикстура, передающая объект класса (см файл конфтест)
def test_4_the_class (fixture_return_class):
    assert fixture_return_class.mod2.pow (2,3) == 8
    assert fixture_return_class.mod1.choice(['a','b', 'c']) == 'a'

def test_5_the_class_2 (fixture_return_class) :
    assert fixture_return_class.hello('Cat') == 'Hello, Cat'