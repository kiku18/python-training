import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
conn=sqlite3.connect('kiku.db')
cur=conn.cursor()
'''
sql='create table if not exists employee(emp_id int,emp_name text,location text,salary text)'
cur.execute(sql)
eid=int(input('enter the id'))
ename=input('enter the name')
elocation=input('enter the location')
salary=float(input('enter the salary'))
sql1=f"insert into employee values({eid},'{ename}','{elocation}',{salary})"
cur.execute(sql1)
conn.commit()
cur.close()
'''
sql='select emp_name,sum(salary) as salary from employee group by emp_name'
query = pd.read_sql_query(sql, conn)
df = pd.DataFrame(query)
print(df)
print(df.head(2))
df.plot(x = 'emp_name', y = 'salary',kind='pie')
plt.show()
cur.execute(sql)
print('-----------------------')
sql='select location,sum(salary) as salary from employee group by location'
query = pd.read_sql_query(sql, conn)
df = pd.DataFrame(query)
print(df)
print(df.tail(2))

df.plot(x = 'location', y = 'salary',kind='bar')
plt.show()
cur.execute(sql)
conn.commit()
cur.close()


