import json
import csv
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
names = json.load(open('first-names.json'))
for i in names:
    customers.append(Customer(names[names.index(i)], membership_types[randrange(5)]))

with open('person.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for j in customers:
        writer.writerow([customers[customers.index(j)].name, customers[customers.index(j)].membership_type])


