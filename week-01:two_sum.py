list_of_people = ["Pramod", "hareesh", "Aishwarya"]
print(list_of_people[1])
print(list_of_people[-2])

list_of_people.append("harshitha")
print(list_of_people)


people_spent = {"Pramod": 4000, "hareesh": 200, "Aishwarya": 300, "harshitha": 0}

people_spent["sumedh"] = 0

total_cost = sum(people_spent.values())
per_person_cost = total_cost / len(people_spent)

for i in people_spent:
    control = people_spent[i] - per_person_cost
    if control > 0:
        print(f"{i} get back {control}")
    elif control < 0:
        print(f"{i} owes {-control}") 
