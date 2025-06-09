if __name__ != "__main__":
    from autograder_assistant import input

def my_len(l_data):
    count = 0
    for item in l_data:
        count = count + 1
    return count


def my_in_list(l_data, target):
    if target in l_data:
        return True
    else:
        return False

def my_location(l_data, target):
    if target in l_data:
        return l_data.index(target)
    else:
        return -1

def my_reverse(l_data):
    l_new = []
    for item in l_data:
        l_new.append(item)
    l_new.reverse()
    return l_new

def my_extrema(l_data):
    return min(l_data), max(l_data)


def my_count(l_data, target):
    appears = 0
    for item in l_data:
        if item == target:
            appears = appears + 1
    return appears

def my_insert(l_data, item, loc):
    l_data.insert(item, loc)
    l_new = []
    for item in l_data:
        l_new.append(item)
    return l_new


def my_remove(l_data, target):
    counter = len(l_data) - 1
    while counter >= 0:
        if l_data[counter] == target:
            del l_data[counter]
        counter = counter - 1
    return l_data

def my_sort(l_data):
    l_data.sort()
    return l_data


def main():
    print()
    

if __name__ == "__main__":
    main()
