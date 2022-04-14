import json
from app import app

def test_home_route():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b'<h1>Todo List</h1>' in response.data


def test_post_route():
    response = app.test_client().post('/add', data=dict(title="Test"))
    assert response.status_code == 200
    assert b'<h1>Todo List</h1>' in response.data
    assert b'Test' in response.data 
    

def test_update_route():
    response = app.test_client().post('/update/1')
    assert response.status_code == 200
    assert b'<h1>Todo List</h1>' in response.data
    assert b'Test' in response.data 
    
def test_delete():
    response = app.test_client().post('/delete/1')
    assert response.status_code == 200
    assert b'<h1>Todo List</h1>' in response.data
    assert b'Test' in response.data