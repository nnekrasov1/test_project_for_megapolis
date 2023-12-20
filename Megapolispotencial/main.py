from names import names
import random
import csv
import names
import generate
import task1

generate.create_dataset()
print(task1.find_res("Ефимов Григорий", "students.csv"))
task1.replace_nones("students.csv", "new_students.csv")
