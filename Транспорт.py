import requests
import xmltojson
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import json

stations = {}


with open("Остановки траллейбусы.json", "r") as json_station:
    station = json.load(json_station)
    stations['Траллейбусы'] = station
    print(str(len(station)) + ' траллейбусных остановок в ФАЙЛЕ!')

with open("Остановки трамваи.json", "r") as json_station:
    station = json.load(json_station)
    stations['Трамваи'] = station
    print(str(len(station)) + ' трамвайных остановок в ФАЙЛЕ!')

print(stations)

def program(number, station):
    import json
    url = "https://online.ettu.ru/station/" + station

    # Headers to mimic the browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/535.36 \
        (KHTML, like Gecko) Chrome/39.0.2171.97 Safari/537.36'
    }

    # Get the page through get() method
    html_response = requests.get(url=url, headers=headers)

    # Save the page content as sample.html
    with open("sample.html", "w") as html_file:
        html_file.write(html_response.text)

    with open("sample.html", "r") as html_file:
        html = html_file.read()
        json_ = xmltojson.parse(html)

    with open("data.json", "w") as file:
        json.dump(json_, file)

    json = json.loads(json_)

    list_tramvai = []
    transport_list = []
    # Получение списка трамваев!
    try:
        for x in json['html']['body']['div']:
            if x == 'p':
                try:
                    super_x = json['html']['body']['div'][x][1]['div']
                    if len(super_x) == 1:
                        list_tramvai.append(super_x['div'])
                    else:
                        for i in super_x:
                            list_tramvai.append(i['div'])

                except:
                    pass

                if len(list_tramvai) > 0:
                    for i in list_tramvai:
                        transport_list.append({'number': i[0]['b'], 'time': i[1]['#text'], 'distance': i[2]['#text']})
                else:
                    transport_list.append('Нет данных')
    except:
        transport_list.append('Пока неизвестная ошибка')

    def where_my_transport(number, station):
        number = str(number)
        text = f"трамвая: {number} нет в списке по остановке: " + stations['Трамваи'][station]

        for i in transport_list:
            if i == 'Нет данных':
                text = i + ' по остановке: ' + stations['Трамваи'][station]
            elif i == 'Пока неизвестная ошибка':
                text = i + ' по остановке: ' + stations['Трамваи'][station]
            else:
                if i['number'] == number:
                    text = i['number'] + ' трамвай будет через: ' + i['time'] + ', на остановке: ' + stations['Трамваи'][station]
                    break
        return text

    return(where_my_transport(number, station))

class MainApp(App):
    def menu_build(self):
        alphavit = ['1', '4', '7', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С',
                    'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Э', 'Ю', 'Я', ]
        print(len(alphavit))
        main_layout = BoxLayout(orientation='vertical')
        str_1 = BoxLayout(orientation='horizontal')
        str_2 = BoxLayout(orientation='horizontal')
        str_3 = BoxLayout(orientation='horizontal')
        id = 0
        for i in alphavit:
            button = Button(text=i)
            button.bind(on_release=self.load_stations)
            if id < 10:
                str_1.add_widget(button)
            elif 9 < id < 21:
                str_2.add_widget(button)
            elif 20 < id < 32:
                str_3.add_widget(button)
            id += 1
        main_layout.add_widget(str_1)
        main_layout.add_widget(str_2)
        main_layout.add_widget(str_3)
        return main_layout

    def build(self):
        self.main_layout = BoxLayout(orientation='vertical')
        self.main_layout.add_widget(self.menu_build())
        return self.main_layout

    def load_stations(self,instation):
        back = Button(text='Назад')
        back.bind(on_release=self.back)
        self.main_layout.clear_widgets()
        text_tramvai = Label(text='Трамвайные остановки:')
        text_tralleibus = Label(text='Траллейбусные остановки:')

        list_tramvai = BoxLayout(orientation='vertical')
        for i in stations['Трамваи'][str(instation.text)]:
            list_tramvai.add_widget(Button(text=str(stations['Трамваи'][str(instation.text)][i])))

        list_tralleibus = BoxLayout(orientation='vertical')
        for i in stations['Траллейбусы'][str(instation.text)]:
            list_tralleibus.add_widget(Button(text=str(stations['Траллейбусы'][str(instation.text)][i])))

        self.main_layout.add_widget(back)
        self.main_layout.add_widget(text_tramvai)
        self.main_layout.add_widget(list_tramvai)
        self.main_layout.add_widget(text_tralleibus)
        self.main_layout.add_widget(list_tralleibus)

    def back(self, instance):
        self.main_layout.clear_widgets()
        self.main_layout.add_widget(self.menu_build())

if __name__ == "__main__":
    app = MainApp()
    app.run()
