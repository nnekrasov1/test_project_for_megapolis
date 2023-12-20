import csv


def find_res(name: str, filename: str) -> str:
    """
    returns the result of the user as:
    Ты получил: <ОЦЕНКА>, за проект - <id>
    :param name:
    :return:
    """

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, ["id", "name", "titleProject_id", "class", "score"])
        for human in reader:
            if name in human["name"]:
                return f"{human['score']}, за проект - {human['titleProject_id']}"


def replace_nones(file_from: str, file_to: str) -> str:
    """
    write data from file_from to file_to replacing
    None in score for the mean of the class
    :param file_from:
    :param file_to:
    :return:
    """

    counts = dict()
    sums = dict()

    with open(file_from, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, ["id", "name", "titleProject_id", "class", "score"])
        for human in reader:
            if human["class"] == "class":
                continue
            if human["score"] == "None":
                continue
            if human["class"] not in counts:
                counts[human["class"]] = 0
                sums[human["class"]] = 0
            counts[human["class"]] += 1
            sums[human["class"]] += int(human["score"])

    with open(file_from, "r", encoding="utf-8") as _from, open(file_to, "w", newline="",
                                                               encoding="utf-8") as _to:
        reader = csv.DictReader(_from, ["id", "name", "titleProject_id", "class", "score"])
        writer = csv.DictWriter(_to, ["id", "name", "titleProject_id", "class", "score"])
        writer.writeheader()

        for human in reader:
            if human["class"] == "class":
                continue
            if human["score"] == "None":
                human["score"] = round(sums[human["class"]] / counts[human["class"]], 3)
            writer.writerow(human)
