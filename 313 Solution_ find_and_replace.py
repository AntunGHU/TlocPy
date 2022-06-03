from nbformat import read


def find_and_replace(file_name, old_word, new_word):
    with open(file_name, "r+") as file:
        text = file.read()
        new_text = text.replace(old_word, new_word)
        file.seek(0)
        file.write(new_text)
        #file.truncate()
        
    with open(file_name) as file:
        text = file.read()
    return text

print(find_and_replace("310 Exercise_ copy.html","class", "atlass"))