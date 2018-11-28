from flask import request

base_url = 'localhost:5000/'

def test_health_endpoint_returns_ok():
    response = request.get(base_url)
    assert response.code == 200

test_health_endpoint_returns_ok()
