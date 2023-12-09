#API

import requests
import os
import json

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

data = []
for i in range(11):
    responce = requests.get('https://api.chucknorris.io/jokes/random')
    if responce.status_code == 200:
        data.append(responce.json())

print(data[:4])
json_file = '\\jokes.json'
with open(__location__ + '\\jokes.json', mode = 'a') as file:
    json.dump(data,file)



#200 = Success
#300 = Redirect 
#400 = Error
#404 = not founded

