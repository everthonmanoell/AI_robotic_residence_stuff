import requests, httpx
#pip install -r requirements.txt
print('requests:', requests.get('https://api.github.com').status_code)
print('httpx   :', httpx.get('https://api.github.com').status_code)