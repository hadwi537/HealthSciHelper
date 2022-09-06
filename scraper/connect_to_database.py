import mysql.connector
from mysql.connector import Error
from pandas import DataFrame
# import MySQLdb

db_host   = '192.168.2.14'
db_name   = 'fvision'
db_user   = 'webuser'
db_passwd = 'insecure_db_pw'

def connect_to_database(df: DataFrame):

    try:
        connection = mysql.connector.connect(host=db_host,
                                            database=db_name,
                                            user=db_user,
                                            password=db_passwd)
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

            df.to_sql(con=connection, name='papers', if_exists='replace', flavor='mysql')

            
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")