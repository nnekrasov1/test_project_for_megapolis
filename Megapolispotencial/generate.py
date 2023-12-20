from names import names
import random
import csv


# https://github.com/Boyarnikov/test_project_for_olimp
# shorturl.at/nqDG1

def generate_dataset(names_):
    """Generates data from names"""
    n = len(names_)
    data = list()
    project_ids = [i for i in range(n)]
    random.shuffle(project_ids)
    class_letters = "аибыжв"
    class_numbers = ["10", "11"]

    for i in range(n):
        human = dict()
        human["id"] = i
        human["name"] = names_[i]
        human["titleProject_id"] = project_ids[i]
        human["class"] = random.choice(class_numbers) + random.choice(class_letters)
        human["score"] = random.randint(20, 100)
        if random.random() < 0.2:
            human["score"] = "None"
        data.append(human)

    return data


def create_dataset():
    """Creates dataset for the project"""
    data = generate_dataset(names)
    with open("students.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, ["id", "name", "titleProject_id", "class", "score"])
        writer.writeheader()
        writer.writerows(data)
