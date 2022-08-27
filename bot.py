import requests
try:
    result = requests.get('https://google.com')
    print(result)
except :
    print('unsuccessful')