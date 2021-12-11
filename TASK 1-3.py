print("--TASK 1--")
class Task_1_Set:
    def __init__(self, arg_1, arg_2, arg_3) -> None:
        self._arg_1 = arg_1
        self._arg_2 = arg_2
        self._arg_3 = arg_3

    def print_args(self):
        print(f"1st arg: {self._arg_1} \n2nd arg: {self._arg_2} \n3rd arg: {self._arg_3} \n")

arg_1 = input("Type in first arg: ")
arg_2 = input("Type in second arg: ")
arg_3 = input("Type in third arg: ")
class_task_1 = Task_1_Set(arg_1, arg_2, arg_3)
class_task_1.print_args()

print("--TASK 2--")
class Monkey:
    max_age = 12
    loves_bananas = True
    def climb(self):
        print('I am climbing the tree')
monkey_1 = Monkey()
monkey_2 = Monkey()
print(f"1st monkey max age = {monkey_1.max_age}, loves banana = {monkey_1.loves_bananas}")
print(f"2nd monkey max age = {monkey_2.max_age}, loves banana = {monkey_2.loves_bananas}")
monkey_1.climb()
monkey_2.climb()

print("--TASK 3--")
class Person:
    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def age_info(self, years):
        age_in_future = self.age + years
        print(f"Person {self.name} / {self.gender} now is {self.age} years \nWill be {age_in_future} in {years}years")

name = input("Type in name: ")
gender = input("Type in gender: ")
while True:
    temp_age = input("Type in age: ")
    try:
        age = int(temp_age)
        break
    except:
        print("Incorrect input")
        continue
test_person = Person(name, age, gender)
while True:
    years_to_past = input("Type in years to past: ")
    try:
        years_to_past = int(years_to_past)
        break
    except:
        print("Incorrect input")
        continue
test_person.age_info(years_to_past)

print("--TASK 5--")
import xlsxwriter

jason = {'first_name': 'Jason', 'last_name': 'Houston', 'age': 29, 'gender': 'male', 'hobby': 'video games', 'job': None}
alice = {'first_name': 'Alice', 'last_name': 'Cooper', 'age': 21, 'gender': 'female', 'hobby': None, 'job': 'software engineer'}

def fill_excel(*args):
    workbook = xlsxwriter.Workbook('hello.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', 'first_name')
    worksheet.write('B1', 'last_name')
    worksheet.write('C1', 'age')
    worksheet.write('D1', 'gender')
    worksheet.write('E1', 'hobby')
    worksheet.write('F1', 'job')

    row = 1

    for item in args:
        worksheet.write(row, 0, item['first_name'])
        worksheet.write(row, 1, item['last_name'])
        worksheet.write(row, 2, item['age'])
        worksheet.write(row, 3, item['gender'])
        worksheet.write(row, 4, item['hobby'])
        worksheet.write(row, 5, item['job'])
        row += 1

    workbook.close()


fill_excel(jason, alice)