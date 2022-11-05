import hidden, psycopg2

secrets_2 = hidden.secrets()

conn_2 = psycopg2.connect(
	host=secrets_2['host'],
	port=secrets_2['port'],
	database=secrets_2['database'],
	user=secrets_2['user'],
	)

cur_2 = conn_2.cursor()

# cur_2.execute('SELECT * FROM account;')
# var_1 = cur_2.fetchall()
# print(var_1)

text_2 = 'acTioN crEaTes mooD'
var_3 = 'INSERT INTO account (content) VALUES (%s);'
cur_2.execute(var_3, (text_2, )) 

conn_2.commit()
cur_2.close()
