def menu():
    filename = "index.txt"
    """
    1. Read
    2. Add
    3. Remove
    4. Replace
    """

    
    return input("Enter choise: ")

    if input == 1:
        pass
    elif input == 2:
        pass
    elif input == 3:
        pass
    elif input == 4:
        pass
    else:
        exit()


def read_file(filename, mode):
    with open (filename, mode) as fd:
        fh = fd.read()
        return fh

def write_to_file(filename, content, mode):
    with open(filename, mode) as fd:
        fd.write(content)

def replace_file():
    item = ""
    result = ""
    while item != "q":
        if result.index[item] == 0:
            result += item
        else:
            result += item + "\n"

if __name__ == "__main__":
    menu()