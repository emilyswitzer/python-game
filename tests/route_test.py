from flask import Flask
import json
from app import Todo
from app import app

def test_home_route():
    app = Flask(__name__)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.status_code == 404

   


def test_post_route():
    app = Flask(__name__)
    client = app.test_client()
    url = '/add'
    response = client.get(url)
    assert response.status_code == 404


    

def test_update_route():
    app = Flask(__name__)
    client = app.test_client()
    url = '/update'
    response = client.get(url)
    assert response.status_code == 404
    
def test_delete():
    app = Flask(__name__)
    client = app.test_client()
    url = '/delete'
    response = client.get(url)
    assert response.status_code == 404