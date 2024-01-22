import requests
import xmltojson
import json

stations = {}
tralleibus = {}
alphavit = ['1', '4', '7', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Э', 'Ю', 'Я']

i1 = [0]
i2 = [0]

for i in alphavit:
    stations[i] = {}
    tralleibus[i] = {}
def bukva(i):
    print('ПАРСИРУЮ БУКВУ:' + i)
    url = "https://m.ettu.ru/stations/" + i

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/535.36 \
            (KHTML, like Gecko) Chrome/39.0.2171.97 Safari/537.36'
    }

    html_response = requests.get(url=url, headers=headers)
    with open("sample.html", "w") as html_file:
        html_file.write(html_response.text)

    with open("sample.html", "r") as html_file:
        html = html_file.read()
        json_ = xmltojson.parse(html)

    with open("data.json", "w") as file:
        json.dump(json_, file)

    json_data = json.loads(json_)
    next_data = json_data['html']['body']['div']['a']
    for str_json in next_data:
        if type(next_data) == dict:
            pass
        elif type(next_data) == list:
            try:
                id = str_json['@href'].split('/')[2]
                if len(id) < 5:
                    stations[str(id)] = str_json['#text']
                    print(f"Автобусная остановка: {str_json['#text']} - добавлена в список!")
                    i1[0] += 1
                else:
                    tralleibus[str(id)] = str_json['#text']
                    print(f"Траллейбусная остановка: {str_json['#text']} - добавлена в список!")
                    i2[0] += 1
            except:
                pass

for i in alphavit:
    bukva(i=i)

list_stations = []

for i in stations:
    list_stations.append(stations[i])

with open("Остановки трамваи.json", "w") as json_station:
    json.dump(stations, json_station)

with open("Остановки траллейбусы.json", "w") as json_station:
    json.dump(tralleibus, json_station)

with open("Остановки траллейбусы.json", "r") as json_station:
    station = json.load(json_station)
    print(str(len(station)) + ' траллейбусных остановок в ФАЙЛЕ!')

with open("Остановки трамваи.json", "r") as json_station:
    station = json.load(json_station)
    print(str(len(station)) + ' трамвайных остановок в ФАЙЛЕ!')

print(len(str(stations)))
print(i1[0])
print(len(str(tralleibus)))
print(i2[0])