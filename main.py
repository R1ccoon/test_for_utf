import requests

url = 'http://127.0.0.1:8000/api/v1/foods/'

response = requests.get(url=url)
print(response.json())
