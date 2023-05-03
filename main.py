with open("shopping-list.txt") as f:
    data = f.readline()
    print(repr(data))