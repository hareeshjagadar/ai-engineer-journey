
party_name = "Pramod Bday"
no_people =5
total_cost=4500
per_person_cost = total_cost / no_people
list_of_people = ["Pramod", "hareesh", "Aishwarya", "harshitha", "Sumedh"]

print(f"{party_name} PARTY")
print(f"{no_people} ARE PRESENT")
print(f"TOTAL SPENT IS {total_cost}")
print(f"PER PERSON COST IS {per_person_cost:.2f}")
print("LIST OF PEOPLE ATTENDING THE PARTY:")
for person in list_of_people:
    print(person)       