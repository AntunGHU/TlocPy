import sqlite3
connection = sqlite3.connect("users.db")
c = connection.cursor()
# query = "CREATE TABLE users (user TEXT, pass INTEGER)"
# c.execute(query)
#query = "INSERT INTO users VALUES('antun2', 'pbantun2')"
#c.execute(query)
u=input("please, enter your name: ")
p=input("please, enter your password: ")    # ' OR 1=1--
u_query = f"SELECT * FROM users WHERE user=? AND pass=?"
c.execute(u_query,(u,p))
result=c.fetchone()
if result:
    print(f"Wellcome back {u}")
else:
    print("Failed login!")
connection.commit()
connection.close()