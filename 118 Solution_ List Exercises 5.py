# Using a nested list comprehension and range(), create a variable called answer  with the following value - [[0, 1, 2], [0, 1, 2], [0, 1, 2]] .  To break it down...start by using range and a list comp to generate the list [0,1,2].  And then repeat that whole thing 3 times in a nested list comp.  It's all a bit tricky to discuss, so maybe it's just best to look at the solution if you get stuck.  

answer =  [[i for i in range(0,3)] for num in range(0,3)]

