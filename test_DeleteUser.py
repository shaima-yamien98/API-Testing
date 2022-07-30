import requests

#API URL
def test_Delete_user();
url = " https://jsonplaceholder.typicode.com/:"
response = requests.delete(url)
#Fetch Response code
print(response.status_code)
assert response.status_code==200

