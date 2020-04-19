# в данном файле описывается конфигурация элементов, используемых в тестах, находящихся в папке с файлов и ниже по иерархии.
# к файлам с тестами, хранящимися выше по иерарзии данный файл не применяется.
# Название файла конфтест должно быть написан с маленькой буквы.
# Тесты ищут условия вверх по каскаду: 1-условия в файле с тестом, 2-условия в папке выше по иерархии, 3-(см. 2).

import pytest
import math
import random


@pytest.fixture()
def fixture_out_1():
    print('printed by fixture_out_1')


@pytest.fixture()
def fixture_return_rnd_number():  # фикстура возвращает рандомное число
    return random.randint(1, 100)


class TestClass:
    def __init__(self, mod1, mod2):
        self.mod1 = mod1
        self.mod2 = mod2

    def hello(self, name):
        return f"Hello, {name}"


@pytest.fixture
def fixture_return_class():
    return TestClass(mod1=random, mod2=math)


@pytest.fixture()
def function_fixture(request):
    print(f"\n Hello from {request.scope} fixture!")

    def fin():
        print(f"\n Finalize from {request.scope} fixture")

    request.addfinalizer(fin)


@pytest.fixture(scope="class")
def class_fixture(request):
    print(f"\n Hello from {request.scope} fixture!")

    def fin():
        print(f"\n Finalize from {request.scope} fixture")

        request.addfinalizer(fin)


#@pytest.fixture(autouse=True) # autouse - исполняется в тестах без вызова
#def autouse_fixture():
 #   print('Print from autouse')
  #  yield
   # print('\nTear down fixture autoused')

@pytest.fixture(params=[11, 12, 13, 14])
def fixture_with_params(request):
    return request.param
