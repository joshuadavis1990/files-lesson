# with open("shopping-list.txt") as f:
#     for line in f:
#         print(f"Item: {line.strip()}")
#     # data = f.readline().strip()
#     # print(data)
#     # print("Hello")

# shows = [
#     "The Mandalorian",
#     "The Witcher",
#     "The X Files",
#     "Star Trek: Picard"
# ]

# with open("tv-shows.txt", "w") as f:
#     f.write("\n".join(shows))

import csv

# with open("people.csv") as f:
#     reader = csv.DictReader(f) # Create a reader object based on the file import
#     for row in reader:
#         # print(row)
#         print(f"{row['name']} is {row['age']} years old and {row['height']}cm tall")

menu = [
    {"item": "Cappucino", "price": 5.50},
    {"item": "English Breakfast Tea", "price": 4},
    {"item": "Blueberry Muffin", "price": 6},
]

with open("cafe-menu.csv", "w") as f:
    writer = csv.DictWriter(f, menu[0].keys())
    writer.writeheader()
    writer.writerows(menu)