import requests
import json

# test the api by collecting data from json file
def test_parameterized_db_API():
    f = open('../json/skechers.json')
    json_data = json.load(f)
    for i in range(0,5):
        response = requests.get("https://66a3-103-137-84-186.ngrok.io/read",params={
            "category" : json_data[i]["category"]
        })
        if  response.status_code !=200: 
            assert response.status_code ==200
    

     


     
