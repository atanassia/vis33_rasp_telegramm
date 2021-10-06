from aiogram import types, Dispatcher
from create_bot import dp, bot

from keyboards import kb_client

# from dstu_timetable import for_oneday, for_week


async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Приветик, дорогой хомячек из моей группы.', reply_markup=kb_client)


async def command_help(message: types.Message):
    await bot.send_message(message.from_user.id, 'Просто не думай, нажимай кнопки и вперед.', reply_markup=kb_client)


# async def send_for_today(message: types.Message):
#     await bot.send_message(message.from_user.id, for_oneday())


# async def send_for_week(message: types.Message):
#     await bot.send_message(message.from_user.id, for_week())


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_help, commands=['help'])
    dp.register_message_handler(send_for_today, commands=['Сегодня'])
    dp.register_message_handler(send_for_tomorrow, commands=['Завтра'])
    dp.register_message_handler(send_for_week, commands=['Неделя'])




import datetime
import requests


DATETODAY = datetime.datetime.now().date()
response = requests.get(f'https://edu.donstu.ru/api/Rasp?idGroup=40208&sdate={DATETODAY}')
data = response.json()


def week_type():
    if data['data']['rasp'][0]['типНедели']%2 == 0:
        return "Нижняя неделя"
    else:
        return "Верхняя неделя"


async def send_for_today(message: types.Message):
    await bot.send_message(message.from_user.id, week_type())
    data_final = ""
    for i in range(len(data['data']['rasp'])):
        if str(DATETODAY) == data['data']['rasp'][i]['дата'][:10]:
            data_final += f"{data['data']['rasp'][i]['дисциплина']}\n\
{data['data']['rasp'][i]['custom1']}\n\
Время - {data['data']['rasp'][i]['начало']} - {data['data']['rasp'][i]['конец']}\n\n"
    if data_final == "":
        data_final = "Нет пар, отдыхаем."
    await bot.send_message(message.from_user.id, data_final)


async def send_for_week(message: types.Message):
    await bot.send_message(message.from_user.id, week_type())
    data_final = ""
    for i in range(len(data['data']['rasp'])-1):
        if data['data']['rasp'][i-1]['день_недели'] == data['data']['rasp'][i]['день_недели']:
            data_final += f"{data['data']['rasp'][i]['дисциплина']}\n\
{data['data']['rasp'][i]['custom1']}\n\
Время - {data['data']['rasp'][i]['начало']} - {data['data']['rasp'][i]['конец']}\n\n"
        else:
            data_final += f"\n\nДень недели - {data['data']['rasp'][i]['день_недели']}\n\n"
    await bot.send_message(message.from_user.id, data_final)


async def send_for_tomorrow(message: types.Message):
    await bot.send_message(message.from_user.id, week_type())
    DATETOMORROW = DATETODAY + datetime.timedelta(days=1)
    data_final = ""
    for i in range(len(data['data']['rasp'])):
        if str(DATETOMORROW) == data['data']['rasp'][i]['дата'][:10]:
            data_final += f"{data['data']['rasp'][i]['дисциплина']}\n\
{data['data']['rasp'][i]['custom1']}\n\
Время - {data['data']['rasp'][i]['начало']} - {data['data']['rasp'][i]['конец']}\n\n"
    if data_final == "":
        data_final = "Нет пар, отдыхаем. "
    await bot.send_message(message.from_user.id, data_final)