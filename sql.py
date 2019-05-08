from mysql.connector import MySQLConnection, Error
from db_config import read_db_config

def connect():
    try:
        dbconfig = read_db_config()
        print('Connecting to DB')
        conn = MySQLConnection(**dbconfig)

        if conn.is_connected():
            print('Connected')
        else:
            print('Connection failed')

    except Error as e:
        print(e)

    finally:
        conn.close()
        print('COnnection closed')

def query_fetchone():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("Select * FROM python_dev")

        row = cursor.fetchone()

        while row is not None:
            print(row)
            row = cursor.fetchone()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def query_fetchall():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM python_dev")
        rows = cursor.fetchall()

        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    query_fetchall()
