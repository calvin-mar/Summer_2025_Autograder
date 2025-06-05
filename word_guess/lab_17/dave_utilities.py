def compare_dicts(dict1, dict2):
    b_same = True
    d1_keys = dict1.keys()
    d2_keys = dict2.keys()
    if len(d1_keys) != len(d1_keys):
        b_same = False
    for k in d1_keys:
        if dict1[k] != dict2[k]:
            b_same = False
    for k in d2_keys:
        if dict1[k] != dict2[k]:
            b_same = False
        
    return b_same
    
def main():
    print()

    

if __name__ == "__main__":
    main()
