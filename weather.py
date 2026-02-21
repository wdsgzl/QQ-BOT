import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_weather(city_code):
    url = f"http://www.weather.com.cn/weather/{city_code}.shtml"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    
    soup = BeautifulSoup(response.text, 'html.parser')
    weather_list = soup.find('ul', class_='t clearfix').find_all('li')
    
    data = []
    for day in weather_list[0:2]:  # 取7天数据
        date = day.find('h1').text
        weather = day.find('p', class_='wea').text
        temp = day.find('p', class_='tem').text.strip()
        
        
        data.append([date, weather, temp])
    
    df = pd.DataFrame(data, columns=['日期', '天气', '温度'])
    return df


