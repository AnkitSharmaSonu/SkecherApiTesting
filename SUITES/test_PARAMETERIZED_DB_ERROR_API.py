import requests
import pyodbc
import configparser

# read databse details
def config():
    config = configparser.ConfigParser()
    config.read("../database/config.ini")
    return config


# get data from database
def get_Data_from_DB():
    con = config()
    server = con["SERVER"]["server"]
    database = con["DB"]["database"]
    username = con["LOGIN"]["login"]
    password = con["PASSWORD"]["password"]
    driver= con["DRIVER"]["driver"]
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * from skecherProductsWithCategory")
            row = cursor.fetchall()
            print("here is the row" , row)
            return row

# test the api with input from db
def test_parameterized_db_API():
    db_data = get_Data_from_DB()
    for i in range(0,5):
      
        response = requests.get("https://66a3-103-137-84-186.ngrok.io/read",params={
            "category" : db_data[i][3] + str("test")
        })
        print("here is the response" , response)
        print("here is the status code" , response.status_code)
        if  response.status_code !=200: 
            assert response.status_code ==200
    

     


     
