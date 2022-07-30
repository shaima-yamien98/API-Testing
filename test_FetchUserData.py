import requests

#API URL
def test_Fetch_user_data();
url = " https://jsonplaceholder.typicode.com/:"
#Send Get Request
response = requests.get(url)

#Display Response Content
print(response.content)
