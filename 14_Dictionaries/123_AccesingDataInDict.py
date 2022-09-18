user_info = {'name': "Blue", "age": 10, "email": "blue@gmail.com"}

print(user_info["name"])
print(user_info["email"])
print(user_info["age"])
print(user_info["auto"])    # KeyError: 'auto'
# ipak dot-pozivanje kao u js u py-a nije moguce! Za razliku od js ovdje moramo quotati
print(user_info.name)
