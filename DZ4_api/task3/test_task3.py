import pytest
import cerberus


@pytest.mark.parametrize('comments',[1,2,3])
def test_task3_1(api_client,comments):
    res = api_client.get(path="posts/{}/comments".format(comments))
    print(res.json())
    schema = {
        "postId": {"type": "integer"},
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "email": {"type": "string"},
        "body": {"type": "string"}
    }
    z = res.json()
    v = cerberus.Validator()
    for i in z:
        assert v.validate(i,schema)


@pytest.mark.parametrize('post_id',[1,2,3])
def test_task3_2(api_client,post_id):
    res = api_client.get(path="posts/{}/comments".format(post_id))
    print(res.json())
    schema = {
        "postId": {"type": "integer","contains": post_id},
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "email": {"type": "string"},
        "body": {"type": "string"}
    }
    z = res.json()
    v = cerberus.Validator()
    for i in z:
        assert v.validate(i,schema)


def test_task3_3(api_client):
    res = api_client.get(path="posts/5")
    print(res.json())
    schema = {
        "userId": {"type": "integer","contains": 1},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    }
    z = res.json()
    v = cerberus.Validator()
    assert v.validate(z,schema)


def test_task3_4(api_client):
        res = api_client.get(path="todos")
        print(res.json())
        schema = {
            "userId": {"type": "integer"},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "completed": {"type": "boolean"}
        }
        z = res.json()
        v = cerberus.Validator()
        for i in z:
            assert v.validate(i,schema)


def test_task3_5(api_client):
    res = api_client.get(path="photos")
    print(res.json())
    schema = {
        "albumId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "url": {'minlength': 8, 'maxlength': 9999},
        "thumbnailUrl": {'minlength': 8, 'maxlength': 9999}
    }
    z = res.json()
    v = cerberus.Validator()
    for i in z:
        assert v.validate(i,schema)