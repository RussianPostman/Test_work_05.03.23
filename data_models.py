from dataclasses import dataclass


@dataclass
class NowWeatherData:
    """Клас для хранения данных ответа эндпоинта:
     - https://api.m3o.com/v1/weather/Now\n
    Эндпоинт возвращает метеоданные на сегодняшний день\n
    Args:
        location: str
        region: str
        country: str
        latitude: float
        longitude: float
        timezone: str
        local_time: str
        temp_c: float
        temp_f: float
        feels_like_c: float
        feels_like_f: float
        humidity: float
        cloud: float
        daytime: bool
        condition: str
        icon_url: str
        wind_mph: float
        wind_kph: float
        wind_direction: str
        wind_degree: float
    """
    location: str
    region: str
    country: str
    latitude: float
    longitude: float
    timezone: str
    local_time: str
    temp_c: float
    temp_f: float
    feels_like_c: float
    feels_like_f: float
    humidity: float
    cloud: float
    daytime: bool
    condition: str
    icon_url: str
    wind_mph: float
    wind_kph: float
    wind_direction: str
    wind_degree: float


@dataclass
class OneDayWeathet:
    """Клас для хранения данных об одном дне из списка,
    возвращаемого эндпоинтом:
     - https://api.m3o.com/v1/weather/Forecast\n
    Эндпоинт возвращает метеоданные на от 1 до 10 дней вперёд\n

    Args:
        date: str
        max_temp_c: float
        max_temp_f: float
        min_temp_c: float
        min_temp_f: float
        avg_temp_c: float
        avg_temp_f: float
        will_it_rain: bool
        chance_of_rain: float
        condition: str
        icon_url: str
        sunrise: str
        sunset: str
        max_wind_mph: float
        max_wind_kph: float
    """
    date: str
    max_temp_c: float
    max_temp_f: float
    min_temp_c: float
    min_temp_f: float
    avg_temp_c: float
    avg_temp_f: float
    condition: str
    icon_url: str
    sunrise: str
    sunset: str
    max_wind_mph: float
    max_wind_kph: float
    will_it_rain: bool = None
    chance_of_rain: float = None


@dataclass
class FutureWeathet:
    """Клас для хранения данных эндпоинта:
     - https://api.m3o.com/v1/weather/Forecast\n
    Эндпоинт возвращает метеоданные на от 1 до 10 дней вперёд\n

    Args:
        location: str
        region: str
        country: str
        latitude: float
        longitude: float
        timezone: str
        local_time: str
        forecast: list[OneDayWeathet]
    """
    location: str
    region: str
    country: str
    latitude: float
    longitude: float
    timezone: str
    local_time: str
    forecast: list[OneDayWeathet]
