import sqlite3
import requests

conn = sqlite3.connect('table.db', 5)
cursor = conn.cursor()
print(conn)

# cursor.execute('''
#   Create table table_2 (
#       column1 TEXT,
#       column2 TEXT,
#       column3 TEXT
# );
# ''')

data = [
    ('link', 'word', 'count')
]

cursor.execute(
    'insert into table_2 (column1, column2, column3) values ("?", "?", "?")'
)

enter = input('Enter your link - ')
requests = requests.get(enter)
text_to_search = input('Enter a word what you wont to search - ')
text = requests.text

count = text.count(text_to_search)
result = []

#print(f'there are {count} words {text_to_search}')