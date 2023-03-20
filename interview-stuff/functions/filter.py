fruit = ["Apple", "Banana", "Appricot"]
filter_obj = filter(lambda s: s[0] == "A", fruit)
print(list(filter_obj))