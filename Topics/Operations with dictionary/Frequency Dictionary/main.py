words = input().lower().split()
my_dict = {key: words.count(key) for key in words}

for key in my_dict:
    print(key + " " + str(my_dict[key]))