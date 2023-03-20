# find the string that contains most words

string_list = [
    "These are some best lines",
    "Possibilities are endless",
    "We are living on round plant and one that is spinning",
    "Responsibilities means ability to respond",
    "If you change you inner life, then there is no such thing as stress"
]

most = max((len(string.split(" ")) for string in string_list))
print(most)

str_1 = (str for str in (max((len(string.split(" ")) for string in string_list))))
print(str_1)
