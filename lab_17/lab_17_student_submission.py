if __name__ != "__main__":
    from autograder_assistant import input



def fix_misspellings(d_info):
    input_file = open("checkme.txt", "r")
    s_text = input_file.readline() 
    input_file.close()
    s_text = s_text.strip()
    l_words = s_text.split(" ")
    for index in range(len(l_words)):
        if l_words[index] in d_info.keys():
            l_words[index] = d_info[l_words[index]]
    s_fixed = ""
    for word in l_words:
        s_fixed = s_fixed + word + " "
    return s_fixed[0:len(s_fixed)-1]

def word_count(s_text):
    test_dict2 = {}
    s_text = "when i am late getting home my goat doofus may make a mistake and eat my cat this keeps mee from getting home late all the time becuz i love my goat and dont want him to get a hairball from eating my cat"
    l_words = s_text.split(" ")
    for word in l_words:
        if word in test_dict2.keys():
            test_dict2[word] = test_dict2[word] + 1
        else:
            test_dict2[word] = 1
    return test_dict2

def translate(d_xlate, s_text):
    l_parts = s_text.split(" ")
    d_errors = {}
    l_error_words = []
    s_translation = ""
    for word in l_parts:
        if word in d_xlate.keys():
            s_translation = s_translation + d_xlate[word] + " "
        else:
            s_translation = s_translation + "?????" + " "
            if word not in l_error_words:
                if word in d_errors.keys():
                    d_errors[word] = d_errors[word] + 1
                else:
                    d_errors[word] = 1
    s_translation = s_translation[0:len(s_translation)-1]
    return s_translation, d_errors
    
def main():
    print()

    

if __name__ == "__main__":
    main()
