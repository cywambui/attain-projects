import sqlite3

conn = sqlite3.connect('trial.db')
f = conn.cursor()

#create table 
#f.execute('''CREATE TABLE hey(morning TEXT, afternoon TEXT, night INT)''')
 
morning = 'hey'
afternoon = 'hello'
night = '20' 

#insert content into table
#f.execute('''INSERT INTO hey VALUES(?, ?, ?)''', (morning, afternoon, night))
#conn.commit()

#f.execute('''SELECT * FROM hey''')
#output = f.fetchall()

#deletes a table from a db
#f.execute('''DROP TABLE hey ''')

#select from specific column
f.execute('''SELECT morning FROM hey''')
output = f.fetchall()
print(output)