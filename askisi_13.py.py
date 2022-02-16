import urllib.request
import json
url='https://drand.cloudflare.com/public/latest '
response=urllib.request.urlopen(url)
html=response.read()
data=html.decode()
kino=json.loads(data)
print(data)
print(kino)