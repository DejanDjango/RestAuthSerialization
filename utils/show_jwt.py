import requests

response = requests.post("http://127.0.0.1:8000/api-token-auth/", data={'username':'dejan','password':'123'})

print(response.text)