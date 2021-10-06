
import datetime
import requests



DATETODAY = datetime.datetime.now().date()
response = requests.get(f'https://edu.donstu.ru/api/Rasp?idGroup=40208&sdate={DATETODAY}')
data = response.json()

async def for_oneday():
    if data['data']['rasp'][0]['типНедели']%2 == 0:
        await ("Нижняя неделя")
    else:
        output_data_week = "Верхняя неделя\n"

    for i in range(len(data['data']['rasp'])):
        if str(DATETODAY) == str(data['data']['rasp'][i]['дата'][:10]):
            output_data = f"Пара в {data['data']['rasp'][i]['день_недели']} -  {data['data']['rasp'][i]['custom1']}\
                Время - {data['data']['rasp'][i]['начало']} - {data['data']['rasp'][i]['конец']}"

    return output_data_week, output_data

def for_week():
    if data['data']['rasp'][0]['типНедели']%2 == 0:
        print("Нижняя неделя\n")
    else:
        print("Верхняя неделя\n")

    for i in range(len(data['data']['rasp'])-1):
        if data['data']['rasp'][i-1]['день_недели'] == data['data']['rasp'][i]['день_недели']:
            print(f"Пара в {data['data']['rasp'][i]['день_недели']} -  {data['data']['rasp'][i]['custom1']}")
        else:
            print(f"\nПара в {data['data']['rasp'][i]['день_недели']} -  {data['data']['rasp'][i]['custom1']}")
        print(f"Время - {data['data']['rasp'][i]['начало']} - {data['data']['rasp'][i]['конец']}")
    return "на неделю"

