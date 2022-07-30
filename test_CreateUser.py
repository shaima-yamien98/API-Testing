import requests
import json 
import jsonpath

#API URL
 def test_create_new_user();
#Read Input Json file
file = open('C:\\Users\\Desktop\\API\\CreateUser.json','r')
json_input = file.read()
request_json = json.loads(json_input)
response = requests.post(url,request_json)
assert response.status_code == 100


def test_other_user();
#Read Input Json file
file = open('C:\\Users\\Desktop\\API\\CreateUser.json','r')
json_input = file.read()
request_json = json.loads(json_input)
response = requests.post(url,request_json)
response_json = json.loads(response.text)
id = jsonpath.jsonpath(response_json , 'id')
print(id[0])
