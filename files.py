def menu():
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

if __name__ == "__main__":
    menu()