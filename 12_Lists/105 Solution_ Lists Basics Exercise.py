# Create a list called instructors
instructors = []
# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"

instructors.append("Colt")
print(instructors)

instructors.append(["Colt", "Blue", "Lisa"])
print(instructors)


instructors.extend(["Colt", "Blue", "Lisa"])
# Run the tests to make sure you've done this correctly!
print(instructors)