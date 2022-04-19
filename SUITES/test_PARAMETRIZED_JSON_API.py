import requests
import json



# test the api by collecting data from json file
def test_parameterized_db_API():
    f = open('./json/skechers.json')
    jsondata = json.load(f)

    test_case = "TC_API_DATA"
   
    for i in range(0,1):
        if test_case ==jsondata[0]["test_case"]:
            response = requests.get("https://d729-103-137-84-186.ngrok.io/read",params={
                "category" : jsondata[i]["category"]
            })
            if  response.status_code !=200: 
                assert response.status_code ==200

            else:
                print("Success")
        else:
            assert "Failure in reading file"


    


     
