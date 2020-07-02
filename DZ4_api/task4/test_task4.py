import pytest
import requests


def test_task4(url, status_code):
    response = requests.get(url + "/".format(status_code))
    assert response.status_code == int(status_code)
