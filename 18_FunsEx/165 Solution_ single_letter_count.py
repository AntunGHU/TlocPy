def single_letter_count(string,letter):
    return string.lower().count(letter.lower())
    
single_letter_count("Hello World", "h") # 1
single_letter_count("Hello World", "z") # 0
single_letter_count("HelLo World", "l") # 3
