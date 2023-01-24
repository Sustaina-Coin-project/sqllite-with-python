#use sql with python (sqllite)
import sqlite3 

connect = sqlite3.connect('data.db')
#drop table if exists
#connect.execute("DROP TABLE IF EXISTS")

# create table with the following parameters
#connect.execute('''CREATE TABLE CUSTOMER 
           # (ID INT  PRIMARY KEY NOT NULL,
            #NAME TEXT NOT NULL,
            #AGE INT NOT NULL);''')


connect.execute("INSERT INTO CUSTOMER (ID,NAME,AGE) VALUES (1, 'CEC', 99) " )
connect.execute("INSERT INTO CUSTOMER (ID,NAME,AGE) VALUES (2, 'NIC', 101) " )

# TO fetch data in the database
all_data = connect.execute('''SELECT * FROM CUSTOMER''')
for row in all_data:
    print(row)
    
connect.close() 

