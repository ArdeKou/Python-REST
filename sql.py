from mysql.connector import MySQLConnection, Error
from db_config import read_db_config

def connect():
    dbconfig = read_db_config()

    try:
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

if __name__ == '__main__':
    connect()
