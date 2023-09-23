import requests

payload = {"firstName":"John","lastName":"Smith"}
r= requests.get("https://httpbin.org/get",params=payload)
print (r.url)
print(r.status_code)
print(r.content)
print(r.text)
