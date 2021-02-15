import json
import csv
f = open('first-names.json')
class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
        print(name, membership_type)
    def upgrade_membership(self, new_membership):
        self.membership_type = new_membership

customers = []
membership_types = ["Bronze", "Silver", "Gold", "Platinum", "Diamond"]
from random import randrange
names = json.load(f)
countagain = 0
for i in names:
    customers.append(Customer(names[countagain], membership_types[randrange(5)]))
    countagain = countagain + 1

count = 0
with open('person.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for j in customers:
        writer.writerow([customers[count].name, customers[count].membership_type])
        count = count + 1


