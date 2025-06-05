def read_data(file_name):
    input_file = open(file_name, "r")
    s_strand = input_file.readline()
    input_file.close()
    s_strand = s_strand.strip()
    return s_strand
    


def main():
    print()

    

if __name__ == "__main__":
    main()
