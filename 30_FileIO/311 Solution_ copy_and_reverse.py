# Write a function called copy_and_reverse, which takes in a file name and a new file name and copies the reversed contents of the first file to the second file.
# Note: we've provided you with the first chapter of Alice's Adventures in Wonderland to give you some sample text to work with. This is also the text used in the tests.
# copy_and_reverse  is very similar to the previous exercise, copy , except that we reverse the text using a slice before we write it to the new file:

def copy_and_reverse(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()

    with open(new_file_name, "w") as new_file:
        new_file.write(text[::-1])


copy_and_reverse('story.txt', 'story_reversed.txt')  # None
# expect the contents of story_reversed.txt to be the reverse of the contents of story.txt
