import requests
import json

file1 = open('captial.csv', 'r')
Lines = file1.readlines()

for line in Lines:
    parameters = {
        'key': 'aBOUYZk70O7rYhUDAAnI5QCUoN8nvtip',
        'location': line
    }

    response = requests.get(
        "http://www.mapquestapi.com/geocoding/v1/address", params=parameters)
    data = json.loads(response.text)['results']

    lat = (data[0]['locations'][0]['latLng']['lat'])
    lng = (data[0]['locations'][0]['latLng']['lng'])

    print("%s %s %s" % (line, lat, lng))
