from typing import List

def read_integers() -> List[int]:
    intp = input()
    strings = intp.split(",")
    num_list = []

    for s in strings:
        num_list.append(int(s))
    
    return num_list
    pass

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
