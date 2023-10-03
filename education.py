# my_dict = {
#     "C1": [10, 20, 30, 7, 6, 23, 90],
#     "C2": [20, 30, 40, 1, 2, 3, 90, 12],
#     "C3": [12, 34, 20, 21],
#     "C4": [22, 54, 209, 21, 7],
#     "C5": [2, 4, 29, 21, 19],
#     "C6": [4, 6, 7, 10, 55],
#     "C7": [4, 8, 12, 23, 42],
#     "C8": [3, 14, 15, 26, 48],
#     "C9": [2, 7, 18, 28, 18, 28],
# }
# my_dict = {key: [value for value in my_dict[key] if value <= 20] for key in my_dict}
# print(my_dict)

emails = {
    "nosu.edu": ["timyr", "joseph", "svetlana.gaeva", "larisa.mamuk"],
    "gmail.com": ["ruslan.chaika", "rustam.mini", "stepik-best"],
    "msu.edu": ["apple.fruit", "beegeek", "beegeek.school"],
    "yandex.ru": ["surface", "google"],
    "hse.edu": ["tomas-henders", "cream.soda", "zivert"],
    "mail.ru": ["angel.down", "joanne", "the.fame.moster"],
}

result = {(emails[key]): key for key in emails}
for res in emails:
    print(res)
