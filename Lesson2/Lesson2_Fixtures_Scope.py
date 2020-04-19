import pytest


def test_one (function_fixture, class_fixture): #module_fixture, session_fixture):
    print ('I test_one NOT in test class 1')

#class TestClass_scopes:
def test_two (function_fixture, class_fixture):
     print('I test_two NOT in test class 2')


