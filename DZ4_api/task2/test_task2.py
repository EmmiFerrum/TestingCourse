import cerberus
import pytest



@pytest.mark.parametrize('types',['micro', 'regional', 'brewpub', 'large'])
def test_task1(api_client,types ):
    res = api_client.get(path="breweries?by_type={}".format(types))
    res_json = res.json()
    for i in res_json:
        assert i['brewery_type'] == types



@pytest.mark.parametrize('id_ok',[1,105,500])
def test_task2_2(api_client,id_ok):
    res = api_client.get(path="breweries/{}".format(id_ok))
    print(res.json())
    schema = {
        "id": {'type': 'integer'},
        "name": {'type': 'string'},
        "brewery_type": {'type': 'string'},
        "street": {'type': 'string'},
        "city": {'type': 'string'},
        "state": {'type': 'string'},
        "postal_code": {'type': 'string'},
        "country": {'type': 'string'},
        "longitude": {'type': 'string'},
        "latitude": {'type': 'string'},
        "phone": {'type': 'string'},
        "website_url": {'type': 'string'},
        "updated_at": {'type': 'string'},
        "tag_list": {'type': 'list'}
    }
    v = cerberus.Validator()
    z = res.json()
    assert v.validate(z,schema)



@pytest.mark.parametrize('id_no_ok',[0,-5,99999999999999999])
def test_task2_3(api_client,id_no_ok):
    res = api_client.get(path="breweries/{}".format(id_no_ok))
    print(res.json())
    schema = {
        "message": {'type': 'string'},
    }
    v = cerberus.Validator()
    z = res.json()
    assert v.validate(z,schema)



@pytest.mark.parametrize('city_no_ok',['abc','dffg','igklo'])
def test_task2_4(api_client,city_no_ok):
    res = api_client.get(path="breweries?by_city={}".format(city_no_ok))
    res_json = res.json()
    assert res_json == []



@pytest.mark.parametrize('city',['Birmingham','Huntsville','Anchorage'])
def test_task2_5(api_client,city):
    res = api_client.get(path="breweries?by_city={}".format(city))
    res_json = res.json()
    for i in res_json:
        assert i['city'] == city
