import pandas
import requests
import json
import time
import random
url = "https://data.mongodb-api.com/app/data-qpjjn/endpoint/data/v1/action/insertOne"

now = pandas.Timestamp(time.ctime())
nowstr = str(now)
randint = random.randint(0,20)

payload = json.dumps({
    "collection": "PeopleCount",
    "database": "data",
    "dataSource": "IOTP-shared",
    "document": {
        "value": randint,
        "timestamp": nowstr
    }
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': 'J3b1RExFRbRYjnfPicNxhaj9Mjbjarlehqf6pzaHgq1vvR9KivPyhyC7clTGFM1Q', 
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)