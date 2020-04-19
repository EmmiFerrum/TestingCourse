import pytest
import random

@pytest.fixture()
def fixture_create_list():
    fruits = ['apple', 'banana', 'pineapple', 'blueberry']
    return fruits


@pytest.fixture()
def fixture_create_set():
    animals = {'cat', 'dog', 'pig', 'lama', 'cow', 'elephant', 'dog', 'lama'}
    return animals


@pytest.fixture()
def fixture_create_set_cute():
    Cute_animals = {'cat', 'dog', 'kenguru', 'turtle'}
    return Cute_animals


@pytest.fixture()
def fixture_mau():
    a = random.randint(1990, 2000)
    b = random.randint(1, 12)
    c = random.randint(1, 31)
   # d = random.randint(1, 100)
    mau = {
        'year': a,
        'month': b,
        'day': c
    }
    return mau

#@pytest.fixture()
#def