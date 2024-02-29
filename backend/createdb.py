import sqlite3

conn = sqlite3.connect("emails.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS emails (
                    email TEXT PRIMARY KEY
                 )''')

conn.commit()
cursor.close()
conn.close()