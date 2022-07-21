# 10'17

import re


def extract_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None


print(extract_phone("my number is 432 555-4242"))   # 432 555-4242
print(extract_phone("my number is 432 555-4242622"))  # None
print(extract_phone("432 555-4242 abcd"))   # 432 555-4242


def extract_phone_all(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    return phone_regex.findall(input)


# ['432 555-4242', '385 312-9888']
print(extract_phone_all("my number is 432 555-4242 ili 385 312-9888"))


def is_valid_phone(input):
    phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
    match = phone_regex.search(input)
    if match:
        return True
    return False


print(is_valid_phone("432 555-4242"))   # True
print(is_valid_phone("432 555-4242 abc"))  # False
print(is_valid_phone(" abcd 432 555-4242"))   # False

# ako ne zelimo dodavati "^" i "$" koristimo metod "fullmatch"


def is_valid_phone(input):
    phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
    match = phone_regex.fullmatch(input)
    if match:
        return True
    return False


print(is_valid_phone("432 555-4242"))   # True
print(is_valid_phone("432 555-4242 abc"))  # False
print(is_valid_phone(" abcd 432 555-4242"))   # False
