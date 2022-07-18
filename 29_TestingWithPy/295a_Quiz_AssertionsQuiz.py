
# * Question 1: Given an example.py  file with the following code:
# ? def say_hi(name):
# ?   assert name == "Colt", "I only say hi to Colt!"
# ?   return f"Hi, {name}!"
# ? print(say_hi("Colt"))
# * What will get output if you run python3 example.py ?
# "Hi, Colt!"
# An assertion error with the message "I only say hi to Colt!"
# "Hi, Charlie!"
# An assertion error with the message "I only say hi to Charlie!"
# * Correct Answer: "Hi, Colt!"

# * Question 2: Given an example.py  file with the following code:
# ? def say_hi(name):
# ?  assert name == "Colt", "I only say hi to Colt!"
# ?  return f"Hi, {name}!"
# ? print(say_hi("Charlie"))
# * What will get output if you run python3 example.py ?
# "Hi, Colt!"
# An assertion error with the message "I only say hi to Colt!"
# "Hi, Charlie!"
# An assertion error with the message "I only say hi to Charlie!"
# * Correct Answer: An assertion error with the message "I only say hi to Colt!"

# * Question 3: Given an example.py  file with the following code:
# ? def say_hi(name):
# ?  assert name == "Colt", "I only say hi to Colt!"
# ?  return f"Hi, {name}!"
# ? print(say_hi("Colt"))
# * What will get output if you run python3 -O example.py ?
# "Hi, Colt!"
# An assertion error with the message "I only say hi to Colt!"
# "Hi, Charlie!"
# An assertion error with the message "I only say hi to Charlie!"
# * Correct Answer:"Hi, Colt!"

# * Question 4: Given an example.py  file with the following code:
# ? def say_hi(name):
# ?  assert name == "Colt", "I only say hi to Colt!"
# ?  return f"Hi, {name}!"
# ? print(say_hi("Charlie"))
# * What will get output if you run python3 -O example.py ?
# "Hi, Colt!"
# An assertion error with the message "I only say hi to Colt!"
# "Hi, Charlie!"
# An assertion error with the message "I only say hi to Charlie!"
# * Correct Answer:"Hi, Charlie!"
