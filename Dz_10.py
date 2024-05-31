import sqlite3
from datetime import datetime
import requests
from bs4 import BeautifulSoup

conn = sqlite3.connect('weather.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS weather (
    datetime TEXT,
    temperature REAL
)
''')

conn.commit()

url = 'https://www.example.com/weather/your-city'  # Заміни на реальний URL

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

temperature_element = soup.find('span', class_='temperature')  # Заміни на правильний селектор
temperature = float(temperature_element.text.strip().replace('°C', ''))

current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

cursor.execute('''
INSERT INTO weather (datetime, temperature) 
VALUES (?, ?)
''', (current_datetime, temperature))

conn.commit()
conn.close()
