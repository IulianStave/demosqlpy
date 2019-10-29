import sqlite3

def create_table():
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert_data(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()
    #prevent SQL injections
    cursor.execute("INSERT INTO store VALUES (?,?,?)",(item, quantity, price))
    conn.commit()
    conn.close()

def view_data():
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    conn.close()
    return rows
def delete_row(item):
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM store WHERE item = ?",(item,))
    conn.commit()
    conn.close()
def update(quantity, price, item):
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE store SET quantity =?, price=? WHERE item = ?",(quantity, price, item))
    conn.commit()
    conn.close()
#insert_data('Water Glass', 42, 6.5)
#insert_data('Coffe cup', 2, 3.5)
print(view_data())
delete_row('wine glasss')
update(20,22,'aa')
delete_row('Coffe cup')
update(20,22,'Water Glass')

print(view_data())
