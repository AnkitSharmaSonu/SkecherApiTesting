import requests
import pyodbc
import configparser
import json
import os

# read databse details
def config():
    config = configparser.ConfigParser()
    path =os.getcwd().replace("\\","/")+ '/database/config.ini'
    # config.read( os.getcwd().replace("\\","\\\\")+ ".\\\\database\\\\config.ini")
    # config.read((os.path.join(os.path.abspath(os.path.dirname(__file__)), 'database\config.ini')).replace("\\","/"))
    # config.read(os.getcwd().replace("\\","\\\\")+ "\\database\\config.ini")
    # config.read(os.path.dirname(os.path.abspath(__file__)),"config.ini")
    # config.read("config.ini")
    # print("here is the path---->>",str(path))
    config.read(path)
    # connection = open(path)
    # config = json.load(connection)
    # config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'database\config.ini'))
    # config.read('./database/config.ini')
    # print("here is the config file----->>>",  config["SERVER"])
    return config

# get data from database
def get_Data_from_DB():
    con = config()
    server = con["SERVER"]["server"]
    # server = "skecherserver.database.windows.net"
    # server = con[0]["server"]
    database = con["DB"]["database"]
    # database = "skecher_db"
    # database = con[0]["database"]
    username = con["LOGIN"]["login"]
    # username = "adminskecher"
    # username = con[0]["login"]
    password = con["PASSWORD"]["password"]
    # password = "skecher@India"
    # password = con[0]["password"]
    driver= con["DRIVER"]["driver"]
    # driver= "{ODBC Driver 17 for SQL Server}"
    # driver= con[0]["driver"]
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * from skecherProductsWithCategory")
            row = cursor.fetchall()
            print("here is the row" , row)
            return row

        
# test the api with input from database
def test_parameterized_db_API():
    db_data = get_Data_from_DB()
    for i in range(0,5):
      
        response = requests.get("https://bea4-103-137-84-186.ngrok.io/read",params={
            "category" : db_data[i][3]
        })
        # print("here is the response" , response)
        # print("here is the status code" , response.status_code)
        if  response.status_code !=200: 
            assert response.status_code ==200


# test_parameterized_db_API()

     


     
