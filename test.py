import sqlite3

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

query = "update sys_command set name = 'excel1' where id = 3" 
cursor.execute(query)

#data = cursor.fetchall()
#print(data)

