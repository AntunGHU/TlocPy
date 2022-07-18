# red phase code:

# ? def eat(food, is_healthy):
# ?     pass
# ?
# ?
# ? def nap(num_hours):
# ?     pass

# green-phase code 2 funkcije

# ? def eat(food, is_healthy):
# ?     ending = "because YOLO!"
# ?     if is_healthy:
# ?         ending = "because my body is a temple!"
# ?     return f"I'm eating {food} {ending}"
# ?
# ?
# ? def nap(num_hours):
# ?     if num_hours == 3:
# ?         return f"Ugh, I overslept. I didn't meant to sleep so long!"
# ?     return f"I'm feeling refreshed after my {num_hours} hour nap!"

# green-phase code 3 funkcije

# ? def eat(food, is_healthy):
# ?     ending = "because YOLO!"
# ?     if is_healthy:
# ?         ending = "because my body is a temple!"
# ?     return f"I'm eating {food} {ending}"
# ?
# ?
# ? def nap(num_hours):
# ?     if num_hours == 3:
# ?         return f"Ugh, I overslept. I didn't meant to sleep so long!"
# ?     return f"I'm feeling refreshed after my {num_hours} hour nap!"
# ?
# ?
# ? def is_funny(person):
# ?     if person == "tim":
# ?         return False
# ?     return True


#  green-phase code 4 funkcije


# ? from random import choice
# ?
# ?
# ? def eat(food, is_healthy):
# ?     ending = "because YOLO!"
# ?     if is_healthy:
# ?         ending = "because my body is a temple!"
# ?     return f"I'm eating {food} {ending}"
# ?
# ?
# ? def nap(num_hours):
# ?     if num_hours == 3:
# ?         return f"Ugh, I overslept. I didn't meant to sleep so long!"
# ?     return f"I'm feeling refreshed after my {num_hours} hour nap!"
# ?
# ?
# ? def is_funny(person):
# ?     if person == "tim":
# ?         return False
# ?     return True
# ?
# ?
# ? def laugh():
# ?     return choice(('lol', 'hahaha', 'thehehe'))
# ?
#  green-phase code 5(6) funkcija


from random import choice


def eat(food, is_healthy):
    if not isinstance(is_healthy, bool):
        raise ValueError("is_healthy must be a boolean!")
    ending = "because YOLO!"
    if is_healthy:
        ending = "because my body is a temple!"
    return f"I'm eating {food} {ending}"


def nap(num_hours):
    if num_hours == 3:
        return f"Ugh, I overslept. I didn't meant to sleep so long!"
    return f"I'm feeling refreshed after my {num_hours} hour nap!"


def is_funny(person):
    if person == "tim":
        return False
    return True


def laugh():
    return choice(('lol', 'hahaha', 'thehehe'))


# def for_error_func(self):
#     if index not in indexOf(l):
#         raise IndexError("index not in l")
