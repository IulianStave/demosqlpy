import psycopg2

print(psycopg2.__version__)

def create_table():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='caterinca77' host='localhost' port='5432'")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert_data(item, quantity, price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='caterinca77' host='localhost' port='5432'")
    cursor = conn.cursor()
    #prevent SQL injections
    cursor.execute("INSERT INTO store VALUES (%s,%s,%s)",(item, quantity, price))
    conn.commit()
    conn.close()

def view_data():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='caterinca77' host='localhost' port='5432'")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    conn.close()
    return rows
def delete_row(item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='caterinca77' host='localhost' port='5432'")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM store WHERE item = %s",(item,))
    conn.commit()
    conn.close()
def update(quantity, price, item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='caterinca77' host='localhost' port='5432'")
    cursor = conn.cursor()
    cursor.execute("UPDATE store SET quantity =%s, price=%s WHERE item = %s",(quantity, price, item))
    conn.commit()
    conn.close()

create_table()
insert_data('Water Glass', 42, 6.5)
insert_data('Coffe cup', 2, 3.5)
print(view_data())
delete_row('wine glasss')
update(20,22,'aa')
delete_row('Coffe cup')
update(20,22,'Water Glass')

print(view_data())
