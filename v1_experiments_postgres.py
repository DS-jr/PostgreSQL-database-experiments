import psycopg2 
import hidden

secrets_1 = hidden.secrets()

conn_1 = psycopg2.connect(    # to confirm PostgreSQL server is running on the specified host & to connect and log in to a PostgreSQL database
    host=secrets_1['host'],
    port=secrets_1['port'],
    database=secrets_1['database'],
    user=secrets_1['user'],
    # password=secrets_1['pass'],  
    connect_timeout=3)

cur_1 = conn_1.cursor()  # cur_1 is a variable name for a database cursor. Cursor allows to send an SQL command and then retrieve the results, perhaps in a loop.

cur_1.execute('SELECT * FROM account;')
rows_1 = cur_1.fetchall() 
#print('seVeraL roWs: ', rows_1) 

var_1 = 'CREATE TABLE if not exists messages_2 (id SERIAL, line TEXT);'
cur_1.execute(var_1)
#print(var_1)
conn_1.commit()  # Flush to the database server

for k in range(2, 6): 
	text_1 = 'keEp pAtieNce ' + str(k)
	var_2 = 'INSERT INTO messages_2 (line) VALUES (%s);'
	cur_1.execute(var_2, (text_1, ))
conn_1.commit() 

var_3 = 'INSERT INTO messages_2 (line) VALUES (%s) RETURNING id;'
cur_1.execute(var_3, (text_1, ))
id = cur_1.fetchone()[0]
print('nEw id', id)

conn_1.commit()
cur_1.close()
