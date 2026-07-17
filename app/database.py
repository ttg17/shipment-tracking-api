import sqlite3

connection = sqlite3.connect("sqlite.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS shipment 
        (id INTEGER, content TEXT, weight REAL, status TEXT)
""")


# cursor.execute("""
#     INSERT INTO shipment VALUES (12703, 'metal gear', 12, 'placed')               
# """)
# connection.commit()


cursor.execute("""
    SELECT * FROM shipment WHERE id = 12703
""")
result = cursor.fetchmany(2)
print(result)

# cursor.execute("DELETE FROM shipment where id == 12701")
# connection.commit()

connection.close()

