# Given a person variable: person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]] 
# Create a dictionary called answer , that makes each first item in each list a key and the second item a corresponding value.  That's a terrible explanation.  I think it'll be easier if you just look at the end goal: {'name': 'Jared', 'job': 'Musician', 'city': 'Bern'} 
# There are many potential solutions for this.
# use the person variable in your answer

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# answer = {k:v for k,v in person}
# answer = {thing[0]: thing[1] for thing in person}
answer = dict(person)
