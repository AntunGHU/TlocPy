# Given two lists ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"] create a dictionary that looks like this {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}. Save it to a variable called answer.
# I expect you to do this with a dictionary comprehension, but you can also use a built-in function called zip .  We cover it later in the course.
# make sure your solution is assigned to the answer variable so the tests can work!

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
answer = {list1[i]: list2[i] for i in range(0,3)}
