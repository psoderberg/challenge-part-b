import random
import json
from faker import Faker
import datetime
fake = Faker()

for x in range(0,200000):
    filename ='./data/hitdata' + str(x) + '.json'
    sesh = random.choice(["S74650220", "S74650221", "S74650222", "S74650223", "S74650224", "S74650225", "S74650226", "S74650220", "S74650221", "S74650220"])
    country = random.choice(["Italy", "France", "Spain"])
    my_dict = {
  "timestamp": str(fake.date_time_between(start_date='-1w', end_date='now').strftime('%Y-%m-%dT%H:%M:%SZ')),
  "session": sesh + str(x),
  #"remote_address": random.choice(["172.31.3.170","173.31.3.170","174.31.3.170"]),
  "remote_address": str(fake.ipv4()),
  "path": random.choice(["http://www.koalastothemax.com/img/koalas3.jpg", "http://www.koalastothemax.com/img/koalas1.jpg", "http://www.koalastothemax.com/img/koalas2.jpg"]),
  "referrer": random.choice(["Direct", "Partner", "Spam"]),
  "timezone_offset": random.choice(["-120", "-60", "-240"]),
  "language": random.choice(["it-IT", "en-EN"]),
  # "city": "Borgo San Lorenzo",
  "city": str(fake.city()),
  "region": "Province of Florence",
  "country": str(fake.country()),
  "continent": random.choice(["Europe", "NA", "SA"]),
  "latitude": random.choice([43.9555,44.6555, 42.9555]),
  "longitude": random.choice([11.3856, 12.3856, 13.3856]),
  "browser": str(fake.firefox()),
  "browser_version": "rv:11.0",
  "agent_type": random.choice(["Browser","Mobile", "Secret"]),
  "agent_category": random.choice(["Personal computer","Autonomous"]),
  "os": random.choice(["Mac", "Windows", "Linux"]),
  "platform": str(fake.mac_processor())
}	
#    print(my_dict)
    with open(filename, 'w') as outfile:
        json.dump(my_dict, outfile)
