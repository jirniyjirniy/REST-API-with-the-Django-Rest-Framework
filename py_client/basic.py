import requests

endpoint = 'http://127.0.0.1:8000/api/'

get_response = requests.post(endpoint, json={"title": 'Hello world'})  # API(application programming interface) -> Method
print(get_response.json())

