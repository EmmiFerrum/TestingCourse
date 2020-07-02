import cerberus
import pytest


def test_task1(api_client):
    res = api_client.get(path="/breed/hound/images/random")
    schema = {
        "message": {"type": "string"},
        "status": {"type": "string"}
    }
    v = cerberus.Validator()
    assert v.validate(res.json(),schema)


def test_task1_2(api_client):
    res = api_client.get(path="/breed/hound/images")
    print(res)
    schema = {
        "message": {"type": "list"},
        "message": {"contains": "https://images.dog.ceo/breeds/hound-afghan/n02088094_1003.jpg"},
        "status": {"type": "string"}
    }
    a = cerberus.Validator()
    assert a.validate(res.json(),schema)


@pytest.mark.parametrize("dogtype",["akita","briard","vizsla"])
def test_task1_3(api_client,dogtype):
    res = api_client.get(path="/breed/{}/images/random".format(dogtype))
    print(res)
    schema = {
        "message": {"type": "string"},
        "status": {"type": "string"}
    }
    a = cerberus.Validator()
    assert a.validate(res.json(),schema)


@pytest.mark.parametrize("countpic",[3,4,5])
def test_task1_4 (api_client, countpic):
    res = api_client.get(path="/breeds/image/random/{}".format(countpic))
    print(res)
    schema = {
        "message": {"type": "list"},
        "status": {"type": "string"}
    }
    a = cerberus.Validator()
    assert a.validate(res.json(),schema)


def test_task1_5(api_client):
    res = api_client.get('/breeds/list/all')
    print(res)
    schema = {
        "message": {"type": "list"},
        "message": {"contains": "akita"},
        "status": {"type": "string"},
    }
    a = cerberus.Validator()
    assert a.validate(res.json(),schema)