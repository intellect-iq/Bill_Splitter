import random

lucky = ""

party_dict = {}

num_of_people = int(input("Enter the number of friends joining (including you): "))

if num_of_people <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line: ")
    for i in range(num_of_people):
        party_dict[input()] = 0
    bill = int(input("Enter the total bill value: "))
    for i in party_dict:
        party_dict[i] = round(bill / num_of_people, 2)
    feature = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: ')
    if feature == "No":
        print("No one is going to be lucky")
        print(party_dict)
    elif feature == "Yes":
        lucky = random.choice(list(party_dict))
        if lucky in party_dict:
            party_dict = {key: round(bill / (num_of_people - 1), 2) for (key, value) in party_dict.items()}
            party_dict[lucky] = 0
            print(f"{lucky} is the lucky one!")
            print(party_dict)
    else:
        print(party_dict)
