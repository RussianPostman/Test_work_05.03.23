import os
import asyncio
from pprint import pprint
from m3o_py.weather import WeatherService
from dotenv import load_dotenv

from data_models import NowWeatherData, FutureWeathet, OneDayWeathet

load_dotenv()

MO3_TOKEN = os.getenv('MO3_TOKEN')
weather = WeatherService(MO3_TOKEN)


async def weather_now(
        location: str = 'london',
        weather: WeatherService = weather
        ) -> NowWeatherData:
    """
    Получить метеоданные на сегодня\n
    Args:
        location: str
        weather: str
    """
    resp = await weather.now(location=location)

    return NowWeatherData(**dict(resp))


async def weather_future(
        location: str = 'london',
        weather: WeatherService = weather,
        days: int = 3
        ) -> NowWeatherData:
    """
    Получить метеоданные на несколько дней вперёд\n
    Args:
        location: str
        days: int > 0 and <= 10
        weather: str
    """
    deys_list = []
    resp = dict(await weather.forecast(location=location, days=days))
    deys = resp.pop('forecast')
    for dey in deys:
        # pprint(dict(dey))
        deys_list.append(OneDayWeathet(**dict(dey)))
    resp['forecast'] = deys_list
    # print(type(deys))

    return FutureWeathet(**resp)


def main():
    """Да, это синхронная ф-ция, нужна просто для демонстрации работы"""
    input_data: str = input(
        'Введиде 1 чтобы получить данные о погоде сегодня\n'
        + 'Введите 2 чтобы получить прогноз погоды\n').strip()
    if input_data not in ['1', '2']:
        print('Вы ввели невалидные данные. Запустите программу заново')

    if input_data == '1':
        pprint(asyncio.run(weather_now()))
    elif input_data == '2':
        pprint(asyncio.run(weather_future()))


if __name__ == '__main__':
    main()
