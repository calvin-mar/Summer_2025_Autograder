if __name__ != "__main__":
    from autograder_assistant import input
def get_data(s_file_name):
    input_file = open(s_file_name, "r")
    l_lines = input_file.readlines()
    for index in range(len(l_lines)):
        if l_lines[index] != "":
            l_lines[index] = l_lines[index].strip()
    if l_lines[len(l_lines)-1] == "":
        del l_lines[len(l_lines)-1]
    input_file.close()
    return l_lines

def count_item_records(s_text, l_data):
    i_count = 0
    for item in l_data:
        if item == s_text:
            i_count = i_count + 1
    return i_count

def count_csv_records(s_text, l_data):
    i_count = 0
    for item in l_data:
        l_pieces = item.split(",")
        for s_part in l_pieces:
            if s_part == s_text:
                i_count = i_count + 1
    return i_count


def make_data_file(s_file_name, l_data):
    output_file = open(s_file_name, "w")
    for index in range(len(l_data) -1):
        output_file.write(l_data[index] + "\n")
    output_file.write(l_data[len(l_data) -1])
    output_file.close()


def make_data_csv_file(s_file_name, i_items_per_line, l_data):
    output_file = open(s_file_name, "w")
    i_items_written = 0
    for item in l_data:
        output_file.write(item)
        i_items_written = i_items_written + 1
        if i_items_written != i_items_per_line:
            output_file.write(",")
        else:
            output_file.write("\n")
            i_items_written = 0

    output_file.close()


def append_to_file(s_file_name, l_data):
    output_file = open(s_file_name, "a")
    output_file.write("\n")
    for item in l_data:
        output_file.write(item)
        output_file.write("\n")
    output_file.close()
    
def main():
    print()

    

if __name__ == "__main__":
    main()
