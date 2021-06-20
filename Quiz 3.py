import requests
import json


url = "https://animechan.vercel.app/api/random"
resp = requests.get(url)
result_json = resp.text
res = json.loads((result_json))
data = requests.get(url).json()
res_structured = json.dumps(res, indent = 4)
print(res_structured)

character = data['character']
quote = data['quote']
print(resp.text)
print(resp.status_code)
print(resp.url)