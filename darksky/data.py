from collections import namedtuple 
from datetime import datetime
import json

features = [
        "date", "meandewpt", "meanpressure", "meantemp", "humidity",
        "maxtemp", "mintemp", "precip", "windspeed", "cloudcover",
        ]

DailySummary = namedtuple("DailySummary", features)  

def parse_all(dates):
    return [parse(d) for d in dates]

def parse(date: datetime) -> DailySummary:
    stamp = str(date).replace(' ', '_')
    filename = 'data/%s.json' % stamp

    with open(filename, 'rb') as f:
        data = json.load(f)['daily']['data'][0]

    try:
        meantemp = (data['temperatureMax'] +data['temperatureMin']) / 2
        summary = DailySummary(
                date=date,
                meandewpt=data['dewPoint'],
                meanpressure=data['pressure'],
                meantemp=meantemp,
                humidity=data['humidity'],
                maxtemp=data['temperatureMax'],
                mintemp=data['temperatureMin'],
                precip=data['precipIntensity'],
                windspeed=data['windSpeed'],
                cloudcover=data['cloudCover'],
                )
    except KeyError as e:
        print('data in file {f} is missing key {k}'.format(f=filename, k=str(e)))
        raise e

    return summary
