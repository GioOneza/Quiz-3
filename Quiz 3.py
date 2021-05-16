import requests
import json

key = '45b568275717c99904f6ca89c278152e'
city = (input("Enter The City: "))
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
resp = requests.get(url)
result_json = resp.text
res = json.loads(result_json)
res_structured = json.dumps(res, indent = 4)
print(res_structured)
m = res['main']
temp = m['temp']
humidity = m['humidity']
print(resp.text)
print(resp.status_code)
print(resp.url)
print('Temperature: ', temp, 'Celsius')
print('Humidty', humidity, '%')
