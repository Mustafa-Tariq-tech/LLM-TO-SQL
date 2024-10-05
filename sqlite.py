import sqlite3
#connect to sqlite 
connection=sqlite3.connect("student.db")

#create a curser object to innsert record , create table 

cursor=connection.cursor()


#create the table 
table_info="""
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25)


);

"""
res = cursor.execute('''SELECT name FROM sqlite_master where name='STUDENT' ''')
if res.fetchone() is None:
    print("created a db")
    cursor.execute(table_info)


#insert the reord in the table


cursor.execute('''Insert Into STUDENT values('ali','Data Science','A') ''')
cursor.execute('''Insert Into STUDENT values('a','d','A') ''')
cursor.execute('''Insert Into STUDENT values('b','c','x') ''')


#DIsplay All th records

data=cursor.execute('''Select * from student''')
for row in data:
    print(row) 

name=cursor.execute('''Select * from STUDENT where NAME='ali' ''')
for n in name:
    print(n)

connection.commit()
connection.close()