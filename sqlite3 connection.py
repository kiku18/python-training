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
sql='select location,sum(salary) as salary from employee group by location'
query = pd.read_sql_query(sql, conn)
df = pd.DataFrame(query)
print(df)
print(df.head(2))
print('-----------------------')
df.plot(x = 'location', y = 'salary',kind='bar')
plt.show()
cur.execute(sql)
conn.commit()
cur.close()


