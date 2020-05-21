import requests
response = requests.get('http://classic.beatport.com/my-beatport?perPage=150')
# print(response)
http_headers = response.headers
# print(http_headers)
# print(http_headers.get('Server'))
print(response.text)
