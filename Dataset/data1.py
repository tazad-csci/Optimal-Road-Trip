import requests
import json

coordinate = []
count = 0

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

    list = []
    lat = (data[0]['locations'][0]['latLng']['lat'])
    lng = (data[0]['locations'][0]['latLng']['lng'])
    list.insert(0, lat)
    list.insert(1, lng)

    print(list)

    coordinate.insert(count, list)
    count += 1
    list.clear()

    # print("%s %s %s" % (line, lat, lng))

# print("The coordinate is : ")
# for i in coordinate:
#     print(i, end=' ')
