import requests
import json



# test the api by collecting data from json file
def test_parameterized_db_API():

    f = open('./json/skechers.json')
    json_data = json.load(f)
    test_case = "TC_ERRORED_API_DATA"
    for i in range(0,1):
        if test_case ==json_data[1]["test_case"]:
            response = requests.get("https://bea4-103-137-84-186.ngrok.io/read",params={
                "category" : str(json_data[i]["category"]) + "test"
            })
            if  response.status_code !=200: 
                assert response.status_code ==200
    

     


     
