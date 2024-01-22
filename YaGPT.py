import requests
def YaGPT():
    prompt = {
        "modelUri": "gpt://b1gj85hbr8si794ga83o/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "system",
                "text": "Ты отвечаешь сообщениями только: [Да / Нет / Не знаю / Спросите по другому / Не скажу]"
            },
            {
                "role": "user",
                "text": "Ты знаешь где взять краба?"
            },
            {
                "role": "assistant",
                "text": "Да"
            },
            {
                "role": "user",
                "text": "И где его взять?"
            },
            {
                "role": "assistant",
                "text": "Не скажу"
            },
            {
                "role": "user",
                "text": "Привет"
            },
        ]
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVN3wdBULPuVLH5-Ep5oidUYz7F5E1zpWPipQZT"
    }

    response = requests.post(url, headers=headers, json=prompt)
    result = response.json()
    if 'error' not in result:
        result = result['result']['alternatives'][0]['message']['text']
    else:
        result = 'Проблемы: ' + str(result)
    print(result)
    return result


YaGPT()


















parametrs = {'Authorization': 'Bearer t1.9euelZqYzJuSis-UjJmUj5CXnZnLne3rnpWanprOz5DLmsuMmoqNzY3PkZPl8_c9bgRU-e9mRA0t_'
                              'd3z930cAlT572ZEDS39zef1656VmpjNzZGbiZCdjsrHnpmZmsaP7_zF656VmpjNzZGbiZCdjsrHnpmZmsaP.'
                              'tY9DYfOSLWBOBLVNZKO3_bt8BGPqlMM8e4wveZgtLJfvHjHKJ55pNiWlf22GkeBpsdrYaVdFRaR4Ybd88JmBDA',
             'x-folder-id': 'b1gj85hbr8si794ga83o'}
'''Идентификатор ключа:
ajedcqd5kbdiq337t2lv
Ваш секретный ключ:
AQVNzWaaWi2y0MZ-ir9sbtNxBEwe54QVKZSS6ea_'''

'''
Идентификатор ключа:
ajev0t0l1cveaiovju2a
Ваш секретный ключ:
AQVN3wdBULPuVLH5-Ep5oidUYz7F5E1zpWPipQZT
Сохраните идентификатор и ключ. После закрытия диалога значение ключа будет недоступно.
'''