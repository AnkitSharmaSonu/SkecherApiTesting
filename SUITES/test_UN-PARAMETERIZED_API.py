import requests

# test the api
def test_unparameterized_API():
    response_API = requests.get("https://d729-103-137-84-186.ngrok.io/read")
    print(response_API.status_code)
    assert response_API.status_code ==200

