import random

special = [33, 35, 36, 37, 38, 42, 43, 60, 64]

# picks a random character from a range using ASCII code
uppercase1 = chr(random.randint(65, 90))
uppercase2 = chr(random.randint(65, 90))
lowercase1 = chr(random.randint(97, 122))
lowercase2 = chr(random.randint(97, 122))
number1 = chr(random.randint(48, 57))
number2 = chr(random.randint(48, 57))
special_char1 = chr(random.choice(special))
special_char2 = chr(random.choice(special))


# generates a password based off random variable from above and randomly shuffles that characters into a random sequence
def create_password():
    password = [uppercase1, lowercase1, lowercase2, special_char1, uppercase2, number1, special_char2, number2]
    shuffle_password = ''.join(random.sample(password, len(password)))
    print(shuffle_password)


create_password()
