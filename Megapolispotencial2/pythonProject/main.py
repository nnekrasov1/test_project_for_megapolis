import random
import string
def generate_login(name: str):
    lastname, name, dads_name = name.split(" ")
    "".capitalize()
    return f"{lastname.capitalize()}_{name[0]}{dads_name[0]}"


def generate_password():
    chars= string.ascii_letters + string.digits
    #return "".join([random.choice(chars) for i in range(8)])
    return "".join(random.choices(chars, k=8))
print(generate_login("Васильев Владимир Богданович"))
print(generate_password())

