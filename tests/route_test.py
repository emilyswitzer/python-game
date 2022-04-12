import json
from app import app

def test_get_all_drinks():
    response = app.test_client().get('/drinks')
    res = json.loads(response.data.decode('utf-8')).get("drinks")
    assert type(res[0]) is dict
    assert type(res[1]) is dict
    assert res[0]['name'] == 'Grape'
    assert res[1]['name'] == 'Lemon'
    assert response.status_code == 200
    assert type(res) is list
    ...