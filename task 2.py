import sqlite3

conn = sqlite3.connect('AnimalKingdom.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS Animals')

cursor.execute('''
    CREATE TABLE Animals (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT,
        Type TEXT
    )
''')

animals_data = [
    ('Лев', 'Ссавець'),
    ('Крокодил', 'Повзун'),
    ('Орел', 'Птах'),
    ('Морська черепаха', 'Повзун'),
    ('Мавпа', 'Ссавець'),
]

cursor.executemany(
    'INSERT INTO Animals (Name, Type) VALUES (?, ?)', animals_data
)

cursor.execute("UPDATE Animals SET Name = 'Сокіл' WHERE Name = 'Орел'")
conn.commit()

print('--- Всі звірі типу "Ссавець" ---')
cursor.execute("SELECT * FROM Animals WHERE Type = 'Ссавець'")
for row in cursor.fetchall():
  print(row)

print('\n--- Всі записи про звірів ---')
cursor.execute('SELECT * FROM Animals')
for row in cursor.fetchall():
  print(row)

conn.close()