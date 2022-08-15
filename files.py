filename = "/home/klt/home/GitHub/test/files_exercise/items.txt"
content = None
mode = None

def menu():

    """
    1. Read
    2. Add
    3. Remove
    4. Replace
    """

    
    return int(input("Enter choise: "))

def choice(inp):
        if inp == 1:
            print(read_file(filename, "r"))
        elif inp == 2:
            write_to_file("\n" + input("Enter item to add: "), "a")        
        elif inp == 3:
            replace_file()
        elif inp == 4:
            delete_items()
        else:
            exit()


def read_file(filename, mode):
    with open (filename, mode) as fd:
        fh = fd.read()
        return fh

def write_to_file(content, mode):
    with open(filename, mode) as fd:
        fd.write(content)

def replace_file():
    item = ""
    result = ""
    while item != "q":
        result += item + "\n"    
        item = input("Add item")
    write_to_file(result, "w")

def delete_items():
    #if inp_item is in list, remove it
    content = read_file(filename, "r")
    remove = input("Enter item to be removed: ")

    if remove in content:
        if content.index(remove) == 0:
            modified_content = content.replace(remove, "")
        else:
            modified_content = content.replace("\n" + remove, "")
        write_to_file(modified_content.strip(), "w") 



if __name__ == "__main__":
    while True:
        choice(menu())
