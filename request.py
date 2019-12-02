import requests

# URL
url = 'http://localhost:5003/api'

# Change the value of experience that you want to test
data = {'age':50, 'salary':50000}

r = requests.post(url,json=data)

print(r.json())

