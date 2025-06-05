
def diff(s_file_name, s_file_name2):
    NO_DIFFS = 0
    DIFFS = 1
    ERROR = 2
    i_num_diffs = 0
    try:
        input_file1 = open(s_file_name)
        input_file2 = open(s_file_name2)

        s_text1 = input_file1.read()
        s_text2 = input_file2.read()
        
        input_file1.close()
        input_file2.close()


        if s_text1 == s_text2:
            return NO_DIFFS
    except:
        return ERROR
    return DIFFS

def main():
    print()

    

if __name__ == "__main__":
    main()
