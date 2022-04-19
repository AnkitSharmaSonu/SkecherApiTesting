import requests

# test the api
def test_unparameterized_API():
    response_API = requests.get("https://bea4-103-137-84-186.ngrok.io/read")
    assert response_API.status_code ==400

